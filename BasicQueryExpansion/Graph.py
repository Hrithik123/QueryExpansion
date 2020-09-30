import matplotlib.pyplot as plt
import csv

x = []
y = []
z = []
with open('collection/datatest.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter='\t')
    for row in plots:
        x.append((row[0]))
        y.append((row[1]))
        z.append((row[2]))
# print(x)
# print(y)
list1 = y
counter = []
listval = []
dateval = []
count = 1
for i in range(len(y)-1):
    if list1[i] == list1[i+1]:
        count+=1
    else:
        listval.append(list1[i])
        counter.append(count)
        dateval.append(z[i])
        count = 1
# sorted(listval)
# sorted(counter).
listval.sort(reverse=True)
counter.sort(reverse=True)
# print(listval)
# print(counter)
# print(dateval)

# print(len(listval))
# print(len(counter))
# print(len(dateval))
l2 = []
l3 = []
for i in range(10):
    l2.append(listval[i])
    l3.append(counter[i])

plt.bar(l2,l3, label='Loaded from file!')
plt.xlabel('Query')
plt.ylabel('Frequency')
plt.title('Top Searched Queries of January-February 2009')
plt.legend()
plt.xticks(rotation=20)
plt.subplots_adjust(bottom=0.3)
plt.show()

l4 = []
l5 = []
for i in range(10,20):
    l4.append(listval[i])
    l5.append(counter[i])

plt.bar(l4,l5, label='Loaded from file!')
plt.xlabel('Query')
plt.ylabel('Frequency')
plt.title('Next top queries')
plt.legend()
plt.xticks(rotation=20)
plt.subplots_adjust(bottom=0.3)
plt.show()

l6 = []
l7 = []
for i in range(len(listval)-20,len(listval)-10):
    l6.append(listval[i])
    l7.append(counter[i])
# print(l6)
# print(l7)

plt.bar(l6,l7, label='Loaded from file!')
plt.xlabel('Query')
plt.ylabel('Frequency')
plt.title('Least Frequent Queries')
plt.legend()
plt.xticks(rotation=20)
plt.subplots_adjust(bottom=0.3)
plt.show()
