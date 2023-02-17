"""Contains the evaluation scripts for comparing predicted and gold IGT"""

from data import IGTLine, load_data_file
from torchtext.data.metrics import bleu_score
import click


def eval_accuracy(pred: list[list[str]], gold: list[list[str]]) -> dict:
    """Computes the average and overall accuracy, where predicted labels must be in the correct position in the list."""
    total_correct_predictions = 0
    total_tokens = 0
    summed_accuracies = 0

    for (entry_pred, entry_gold) in zip(pred, gold):
        entry_correct_predictions = 0

        for token_index in range(len(entry_gold)):
            # For each token, check if it matches
            if token_index < len(entry_pred) and entry_pred[token_index] == entry_gold[token_index]:
                entry_correct_predictions += 1

        entry_accuracy = (entry_correct_predictions / len(entry_gold))
        summed_accuracies += entry_accuracy

        total_correct_predictions += entry_correct_predictions
        total_tokens += len(entry_gold)

    total_entries = len(gold)
    average_accuracy = summed_accuracies / total_entries
    overall_accuracy = total_correct_predictions / total_tokens
    return {'average_accuracy': average_accuracy, 'accuracy': overall_accuracy}


def eval_stems_grams(pred: list[list[str]], gold: list[list[str]]) -> dict:
    perf = {'stem': {'correct': 0, 'pred': 0, 'gold': 0}, 'gram': {'correct': 0, 'pred': 0, 'gold': 0}}

    for (entry_pred, entry_gold) in zip(pred, gold):
        for token_index in range(len(entry_gold)):

            # We can determine if a token is a stem or gram by checking if it is all uppercase
            token_type = 'gram' if entry_gold[token_index].isupper() else 'stem'
            perf[token_type]['gold'] += 1

            if token_index < len(entry_pred):
                pred_token_type = 'gram' if entry_pred[token_index].isupper() else 'stem'
                perf[pred_token_type]['pred'] += 1

                if entry_pred[token_index] == entry_gold[token_index]:
                    # Correct prediction
                    perf[token_type]['correct'] += 1

    stem_perf = {'prec': perf['stem']['correct'] / perf['stem']['pred'],
                 'rec': perf['stem']['correct'] / perf['stem']['gold']}
    stem_perf['f1'] = 2 * (stem_perf['prec'] * stem_perf['rec']) / (stem_perf['prec'] + stem_perf['rec'])
    gram_perf = {'prec': perf['gram']['correct'] / perf['gram']['pred'],
                 'rec': perf['gram']['correct'] / perf['gram']['gold']}
    gram_perf['f1'] = 2 * (gram_perf['prec'] * gram_perf['rec']) / (gram_perf['prec'] + gram_perf['rec'])
    return {'stem': stem_perf, 'gram': gram_perf}


def eval_morpheme_glosses(pred_morphemes: list[list[str]], gold_morphemes: list[list[str]]):
    """Evaluates the performance at the morpheme level"""
    morpheme_eval = eval_accuracy(pred_morphemes, gold_morphemes)
    class_eval = eval_stems_grams(pred_morphemes, gold_morphemes)
    bleu = bleu_score(pred_morphemes, [[line] for line in gold_morphemes])
    return {'morpheme_level': morpheme_eval, 'classes': class_eval, 'bleu': bleu}


@click.command()
@click.option("--pred", help="File containing predicted IGT", type=click.Path(exists=True), required=True)
@click.option("--gold", help="File containing gold-standard IGT", type=click.Path(exists=True), required=True)
def evaluate_igt(pred: str, gold: str):
    """Performs evaluation of a predicted IGT file"""

    pred = load_data_file(pred)
    gold = load_data_file(gold)

    pred_words = [line.gloss_list() for line in pred]
    gold_words = [line.gloss_list() for line in gold]
    word_eval = eval_accuracy(pred_words, gold_words)

    pred_morphemes = [line.gloss_list(segmented=True) for line in pred]
    gold_morphemes = [line.gloss_list(segmented=True) for line in gold]

    all_eval = {'word_level': word_eval, **eval_morpheme_glosses(pred_morphemes=pred_morphemes, gold_morphemes=gold_morphemes)}
    print(all_eval)


if __name__ == '__main__':
    evaluate_igt()
