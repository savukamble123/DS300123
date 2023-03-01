x = [(2,5),(1,2),(4,4),(2,3),(2,1)]
for i in range(len(x)):
    for j in range(len(x)):
        if x[i][1]<x[j][1]:
            x[i],x[j] = x[j],x[i]
print(x)            
