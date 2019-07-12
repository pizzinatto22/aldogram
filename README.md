# aldogram
A simple dendrogram implementation for pattern recognition (clustering).

This program aims to cluster some input data showing the best classes. It connects the most similar elements considering every field record.


This implementation show an horizontal red line, considered as *cutting point*. The number of vertical lines crossed by this red line, means the ideal number of classes (and its elements!).

# Authors
Luiz Eduardo Pizzinatto

&

Bruno Martins Crocomo

# Execution

```
python3 dendrogram.py <csv file> <1|2>
```

where:
```
csv file is an input file, separated by ; and header names in first row
1 or 2 is class distance connection type:
   1 - Simple distance (shortest distance between neighbours)
   2 - Complete distance (longest distance between neighbours)
```

For comparison purposes, there is a file `ex.py` wich execute the same, but with a well known library. It supposed to use only simple distance (so, the last parameter is not considered).

# Examples
There are some test files inside `datasets` folder.

```
[aldogram]$ python3 dendrogram.py datasets/iris.csv 2
(0.0, 7.439455625245708)
cut point:  5.555059096533482
```
![iris result](/datasets/iris.png)

As the horizontal red line cross two vertical lines (at point 5.555059096533482), two classes would be ideal, where each branch has its own elements.

# Infos
Field names as `#`, `class` and `valid` will not be considered.
There is a heuristic for calculating the cutting point, available bellow, in Portuguese.

```
A heurística para chegar a este ponto de corte foi a seguinte:
    - Calcula-se a maior distância entre um ponto de linkagem e os 2 pontos de linkagem dos seus sub-ramos, isto é, se houve um ponto
      linkagem no ponto 10 de duas classes, mas seus ramos tiveram linkagem em 6 e 3, então as distâncias entre esses pontos é 4 e 7.
      Neste caso, a maior distância de linkagem é 7 (distância entre o topo da classe pai e a classe filho mais baixa). Define-se como ponto de corte o ponto médio entre 7 e 10, nesse caso, 8.5.
```
