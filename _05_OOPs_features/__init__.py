l1 = [1,2,3,4,5,6,7,8]

k = 3
li2 = []
for i in range(0, len(l1), k):
    data = l1[i:i+3]
    if len(data) == k:
        data.sort(reverse=True)
    li2.append(data)
print(li2)