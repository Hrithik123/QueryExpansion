import matplotlib.pyplot as plt
import csv

x = []
y = []
z = []
with open('collection/dataset.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter='\t')
    for row in plots:
        x.append(int(row[0]))
        y.append((row[1]))
        z.append((row[2]))

print(y)
print("--------------------")
print(z)
p=[]
q=[]
r = []
s = []
for i in reversed(range(10)):
    p.append(y[i])
    q.append(z[i])
for i in reversed(range(10,20)):
    r.append(y[i])
    s.append(z[i])
plt.bar(p,q, label='Loaded from file!')
plt.xlabel('Query')
plt.ylabel('Frequency')
plt.title('Top Queries Hit Frequencies')
plt.legend()
plt.show()

plt.bar(r,s, label='Loaded from file!')
plt.xlabel('Query')
plt.ylabel('Frequency')
plt.title('Next Top Queries Hit Frequencies')
plt.legend()
plt.show()