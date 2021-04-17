#cross product
import numpy as np

print("input two vectors:  ")

#take array inputs
print("vector 1(x,y,z): ")
ar1=[]
for i in range(0,3):
    inp = float(input())
    ar1.append(inp)

print("vector 2(x,y,z): ")
ar2=[]
for i in range(0,3):
    inp = float(input())
    ar2.append(inp)

cp=[]    
cp.append(ar1[1]*ar2[2] - ar1[2]*ar2[1])
cp.append(-ar1[0]*ar2[2] + ar1[2]*ar2[0])
cp.append(ar1[0]*ar2[1] - ar1[1]*ar2[0])
print('Manual:',cp[0],'i +',cp[1],'j +', cp[2],'k ')
print('Numpy:',np.cross(ar1,ar2))

