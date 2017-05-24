import numpy as np
i=input("Please enter the first number\n")
g=input("Please enter the second number\n")
m1=np.arange(i,g+1)
d=m1.size
if(d%2==0):
 q1=d/2
 m1=m1.reshape(2,q1)
else:
 q2=d/2
 q3=q2+1
 m1=np.append(m1,0)
 m1=m1.reshape(2,q3)
print "The array is\n",m1
a=input("Enter the first number\n")
b=input("Enter the second number\n")
m1=m1.ravel()
s=m1.size
c1=m1%a==0
c2=m1%b==0
for i in range(s):
 if c1[i]==c2[i]:
  if c1[i]==True:
   print m1[i]

