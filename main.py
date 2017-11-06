import DataCollector
from sklearn.neural_network import MLPClassifier

MLP = MLPClassifier((20, 20, 20), "logistic", "sgd", 0.0001, "auto", "constant")
print(DataCollector.formFilePath(2, 5))
DataCollector.formTeachingArray()
print(DataCollector.Y)
#print(DataCollector.getListFromPGM(DataCollector.curfile))