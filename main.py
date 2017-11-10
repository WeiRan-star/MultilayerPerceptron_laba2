import DataCollector
from sklearn.neural_network import MLPClassifier

MLP = MLPClassifier((20, 20, 20), "logistic", "sgd", 0.0001, "auto", "constant")
DataCollector.formTeachingArray()
DataCollector.normalizeTeachingArray()
# print(len(DataCollector.X))
# print(len(DataCollector.X[2]))
# print(len(DataCollector.Xnorm))
# print(len(DataCollector.Xnorm[2]))
MLP.fit(DataCollector.Xnorm, DataCollector.Y)
MLP.predict(DataCollector.getListFromPGM(DataCollector.formFilePath(1, 8)))
print(DataCollector.formFilePath(2, 5))
DataCollector.formTeachingArray()
# print(DataCollector.X[0][0])
# print(DataCollector.Xnorm[0][0])
# print(DataCollector.Y)
# print(DataCollector.Ynorm)
#print(DataCollector.getListFromPGM(DataCollector.curfile))