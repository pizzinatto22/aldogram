from matplotlib.pyplot import show
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.spatial.distance  import pdist
import sys
import csv

f = csv.DictReader(open(sys.argv[1]), delimiter=';')
fields = f.fieldnames

data = []

for row in f:
    r = []
    for field in fields:
        if field not in ['class']: 
            r.append(float(row[field]))
    data.append(r)

Y = pdist(data)
Z = linkage(Y)
print(Z)
dendrogram(Z)

show()
