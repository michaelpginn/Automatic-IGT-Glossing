# Automatic-IGT-Glossing
This repository provides the baseline system for the task https://github.com/sigmorphon/2023glossingST. 

Train model:

```shell
python3 token_class_model.py train --lang ddo --track open
```

Make predictions:

```shell
python3 token_class_model.py predict --lang ddo --track open --pretrained_path ./output --data_path ../../GlossingSTPrivate/splits/Tsez/ddo-dev-track1-covered
```

Eval predictions:

```shell
python3 eval.py --pred ./predictions --gold ../../GlossingSTPrivate/splits/Tsez/ddo-train-track1-uncovered
```

## Model design

## Results

Trained models: [download here](https://o365coloradoedu-my.sharepoint.com/:f:/g/personal/migi8081_colorado_edu/EhzVMGQwS_5GuV4R1BZYbVIBJbj0zHi09t85zGRuAwEkbw?e=iEIIfH)

### Dev Performance
#### Closed Track
| Lang | Morpheme Acc| Word Acc | BLEU (Morpheme) | Stems | Grams |
| --- | --- | --- | --- | --- | --- |
| ddo | Ovr: 47.5<br>Avg: 52.9 | Ovr: 71.8<br>Avg: 72.1 | 57.8 | P: 49.7<br>R: 49.2<br>F1: 49.4 | P: 50.7<br>R: 46.1<br>F1: 48.3 |
| git | Ovr: 13.6<br>Avg: 16.3 | Ovr: 26.5<br>Avg: 29.1 | 4.5 | P: 6.7<br>R: 5.8<br>F1: 6.2 | P: 22.2<br>R: 17.6<br>F1: 19.7 |]
| lez | Ovr: 48.1<br>Avg: 49.2 | Ovr: 56.9<br>Avg: 55.7 | 52.0 | P: 54.0<br>R: 51.3<br>F1: 52.6 | P: 53.5<br>R: 40.7<br>F1: 46.2 |
| nyb | Ovr: 77.1<br>Avg: 78.2 | Ovr: 83.9<br>Avg: 82.4 | 74.2 | P: 86.2<br>R: 78.7<br>F1: 82.3 | P: 78.6<br>R: 75.3<br>F1: 76.9 |
| usp | Ovr: 63.1<br>Avg: 65.5 | Ovr: 74.0<br>Avg: 70.3 | 53.8 | P: 72.0<br>R: 62.7<br>F1: 67.0 | P: 61.3<br>R: 63.7<br>F1: 62.4 |

#### Open Track
| Lang | Morpheme Acc| Word Acc | BLEU (Morpheme) | Stems | Grams |
| --- | --- | --- | --- | --- | --- |
| ddo | Ovr: 85.0<br>Avg: 86.0 | Ovr: 74.2<br>Avg: 75.8 | 68.6 | P: 89.3<br>R: 86.6<br>F1: 87.9 | P: 82.2<br>R: 83.6<br>F1: 82.9 |

