from __future__ import print_function
import DataCollector as DC
from sklearn.neural_network import MLPClassifier

print("I've launched.")
MLP = MLPClassifier(hidden_layer_sizes=(120, 40), solver='sgd', verbose=True, tol=0.00001,
                    max_iter=1500, alpha=0.01, learning_rate_init=0.01, learning_rate='adaptive')
#MLPClassifier((20, 20, 20), "logistic", "sgd", 0.0001, "auto", "constant")
print("Forming teaching arrays.")
DC.formTeachingArray()
DC.normalizeTeachingArray()
# print(len(DC.X))
# print(len(DC.X[2]))
# print(len(DC.Xnorm))
# print(len(DC.Xnorm[2]))
print("Fitting.")
MLP.fit(DC.Xnorm, DC.Y)
# CurrentDataSet = DC.getListFromPGM(DC.formFilePath(1, 8))
# crap = DC.normalizeList(CurrentDataSet)
# print(MLP.predict(crap))
# crap2 = DC.getPGMAndNormalize(1, 8)
# print(MLP.predict(crap2))
# crap2 = DC.getPGMAndNormalize(2, 8)
# print(MLP.predict(crap2))
# crap2 = DC.getPGMAndNormalize(3, 8)
# print(MLP.predict(crap2))

for currFace in range(1, 41):
    print("Next 3 numbers should be {0}:".format(currFace))
    for currPic in range(8, 11):
        currentRecogn = DC.getPGMAndNormalize(currFace, currPic)
        print(MLP.predict(currentRecogn), end='')
    print(" ")


# print(DC.formFilePath(2, 5))
# DC.formTeachingArray()
# print(DC.X[0][0])
# print(DC.Xnorm[0][0])
# print(DC.Y)
# print(DC.Ynorm)
#print(DC.getListFromPGM(DC.curfile))