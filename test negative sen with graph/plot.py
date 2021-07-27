import matplotlib.pyplot as plt
import csv
import itertools
x = []
y = []

with open('names.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append((row[0]))
        y.append((row[1]))
        
lists = sorted(zip(*[x, y]))
new_x, new_y = list(zip(*lists))

plt.bar(new_x,new_y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.tight_layout()
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
