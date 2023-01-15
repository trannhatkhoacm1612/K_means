import numpy as np
import matplotlib.pyplot as plt

X = np.asarray([1,2,4,5])
Y = np.asarray([1,1,3,4])

def euclid_dis(x,y):
    return (x[0] - y[0] )**2 + (x[1] - y[1]) ** 2
C1 = (X[0],Y[0])
C2 = (X[3],Y[3])
while True:
    
    print(C1,C2)
    C1_dis = C2_dis = np.array([])

    for i in range(4):
        C1_dis = np.insert(C1_dis,i,euclid_dis((X[i],Y[i]),C1))
        C2_dis = np.insert(C2_dis,i,euclid_dis((X[i],Y[i]),C2))
        if C1_dis[i] <= C2_dis[i]:
            C1_dis[i] = 1
            C2_dis[i] = 0
        else:
            C1_dis[i] = 0
            C2_dis[i] = 1
    C1_clus = []
    C2_clus = []

    for i in range(4):
        if C1_dis[i] == 1:
            C1_clus.append((X[i],Y[i]))
        else:
            C2_clus.append((X[i],Y[i]))

    C1_new = ((C1_clus[0][0] + C1_clus[1][0]) / 2,(C1_clus[0][1] + C1_clus[1][1]) / 2)
    C2_new = ((C2_clus[0][0] + C2_clus[1][0]) / 2,(C2_clus[0][1] + C2_clus[1][1]) / 2)
    if C1_new == C1 and C2_new == C2:
        print('khoa')
        break
    C1 = C1_new
    C2 = C2_new
fig, ax = plt.subplots()
plt.plot(X,Y,'b^',markersize = 4, alpha = .8)
plt.plot(C1[0],C1[1],'go',markersize = 4,)
plt.plot(C2[0],C2[1],'rs',markersize = 4,)
ax.plot((2,4),(3.45, 1.05))
plt.plot((C1[0] + C2[0]) / 2,(C1[1] + C2[1]) / 2,'go',markersize = 4)
plt.show()

# 3,2.5 -> 6,5 6x + 5y - 29.25 -> (0,5.85) (4, 1.05) 