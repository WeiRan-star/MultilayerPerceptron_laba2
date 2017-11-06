import DataCollector
from sklearn.neural_network import MLPClassifier

MLP = MLPClassifier((20, 20, 20), "logistic", "sgd", 0.0001, "auto", "constant")
print(DataCollector.read_pgm(DataCollector.pil_currentfile))