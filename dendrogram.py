#from matplotlib.pyplot import show
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram

import sys
import csv
import operator
import math

def euclidean(x, y):
    distance = 0
    for key in x.keys():
        if key not in ['#','class', 'valid']:
            distance += (float(x[key]) - float(y[key])) ** 2
    
    return math.sqrt(distance)

    
def class_distance(c1, c2, distances, func):
    i = c1[0]['#']
    j = c2[0]['#']
    
    distance = distances[i][j]

    for x in c1:
        for y in c2:
            i = x['#']
            j = y['#']

            distance = func(distance,distances[i][j])

    return distance


f = csv.DictReader(open(sys.argv[1]), delimiter=';')

if sys.argv[2] == '1':
    func = min
else:
    func = max

classes = []

i = 0
for row in f:
    row['#'] = i
    classes.append([[row],i])
    i += 1



#calcule all distances
classes_len = len(classes)
distances = []
for i in range (0, classes_len):
    row = []
    for j in range (0, classes_len):
        row.append(0)
    distances.append(row)

#in each class we have just one element, so we can access element [0]
for i in range(0, classes_len - 1):
    for j in range(i + 1, classes_len):
        distances[i][j] = euclidean(classes[i][0][0], classes[j][0][0])
        distances[j][i] = distances[i][j]


hierarchy     = []
qt_classes    = len(classes)
valid_classes = classes_len

#cluster
while valid_classes > 1:
    i = 0

    min_distance = sys.float_info.max
    min_index1    = -1
    min_index2    = -1

    #find nearest neighbour pair
    for i in range(0, valid_classes - 1):
        for j in range(i + 1, valid_classes):
            d = class_distance(classes[i][0], classes[j][0], distances, func)
            
            if (d < min_distance):
                min_distance = d
                min_index1 = i
                min_index2 = j
    
    #then, put this 2 classes together in a new class
    c1 = classes[min_index1]
    c2 = classes[min_index2]
    cluster = c1[0] + c2[0] 
    classes.append([cluster, qt_classes])
    hierarchy.append([c1[1], c2[1], #original index of this classes 
                        float(min_distance),
                        len(cluster)])

    del classes[max(min_index1, min_index2)]
    del classes[min(min_index1, min_index2)]

    valid_classes -= 1
    qt_classes    += 1 

max_distance = 0
cut_point    = 0

for h in hierarchy:
    if h[0] < classes_len:
        d0 = 0
    else:
        d0 = hierarchy[h[0] - classes_len][2]

    if h[1] < classes_len:
        d1 = 0
    else:
        d1 = hierarchy[h[1] - classes_len][2]

    maximum = max(h[2] - d0, h[2] - d1)

    if maximum > max_distance:
        max_distance = maximum
        cut_point    = 0.5 * (max(d0, d1) + h[2])

#fig, ax = plt.subplots()
dendrogram(hierarchy)
print(plt.ylim())
print("cut point: ",cut_point)
plt.plot(plt.xlim(), [cut_point, cut_point], 'r-')
plt.show()
