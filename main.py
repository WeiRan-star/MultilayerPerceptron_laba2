from __future__ import print_function
import DataCollector as DC
from PIL import Image
from sklearn.neural_network import MLPClassifier

# a = DC.glueTwoImages(1,1,1,5)
# a.show()
# a.save("guessed/a.bmp")
# input("STOP ME NOW")


print("I've launched.")

MLP = MLPClassifier(hidden_layer_sizes=(120, 40), solver='sgd', verbose=True, tol=0.00001,
                    max_iter=150, alpha=0.01, learning_rate_init=0.01, learning_rate='adaptive')

print("Forming teaching arrays.")
DC.formTeachingArray()
DC.normalizeTeachingArray()

print("Fitting.")
MLP.fit(DC.Xnorm, DC.Y)

for currFace in range(1, 41):
    print("Next 3 numbers should be {0}:".format(currFace))
    for currPic in range(8, 11):
        currentRecogn = DC.getPGMAndNormalize(currFace, currPic)
        currentGuess = (MLP.predict(currentRecogn))[0]
        DC.glueTwoImages(currFace, currPic, currentGuess, 1).save("guessed/f{0}p{1}.bmp".format(currFace, currPic))
        print(currentGuess, end='')
    print(" ")
