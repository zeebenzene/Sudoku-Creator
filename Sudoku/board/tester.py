
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans, vq
from matplotlib.mlab import PCA

from solver import solve
from board import Board

def createElbowGraph(data):
    kvals = []
    dists = []
    for k in range(2,10):
        centroids, distortion = kmeans(data, k)
        kvals.append(k)
        dists.append(distortion)
    plt.plot(kvals, dists)
    plt.show()


removedAndDifficulties= []

for removenum in range(25, 35):
    for i in range(100):
        b = Board('')
        b.createEmptySpaces(81-removenum)
        difficulty = solve(b)
        removedAndDifficulties.append((removenum, difficulty))

def getIdxFromTup(tuples, idx):
    second = []
    for tup in tuples:
        second.append(tup[idx])
    return second

difficulties = getIdxFromTup(removedAndDifficulties, 1)
difficulties = np.array(difficulties)

createElbowGraph(difficulties)


centroids, distortion = kmeans(difficulties, 4)
idx, _ = vq(difficulties, centroids)

print 'started clustering'
clusterings = {}
diff = {}
clusterings[0] = []
clusterings[1] = []
clusterings[2] = []
clusterings[3] = []

diff[0] = []
diff[1] = []
diff[2] = []
diff[3] = []

for i in range(len(idx)):
    indx = idx[i]
    clusterings[indx].append(removedAndDifficulties[i][0])
    diff[indx].append(removedAndDifficulties[i][1][0])


print(clusterings)
plt.hist(clusterings[0])
plt.show()
print "Average Difficulty for cluster 0: " + str((sum(diff[0]) / float(len(diff[0]))))

plt.hist(clusterings[1])
print "Average Difficulty for cluster 1: " + str((sum(diff[1]) / float(len(diff[1]))))
plt.show()

plt.hist(clusterings[2])
print "Average Difficulty for cluster 2: " + str((sum(diff[2]) / float(len(diff[2]))))
plt.show()

plt.hist(clusterings[3])
print "Average Difficulty for cluster 3: " + str((sum(diff[3]) / float(len(diff[3]))))
plt.show()