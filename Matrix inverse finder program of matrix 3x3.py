#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
print('###----- Inverse Finder of 3x3 Matrix ----- ####')
print('Enter Matrix in Format : ')
print('enter row 1 :-  2,4,5')
print('enter row 2 :- -2,7,3')
print('enter row 3 :- 9,0,-1')
print()
a=input('enter Row 1 :-  ')
aa=a.split(",")
for i in range(len(aa)):
    aa[i]=int(aa[i])
b=input('enter Row 2 :-  ')
bb=b.split(",")
for i in range(len(bb)):
    bb[i]=int(bb[i])
c=input('enter Row 3 :-  ')
cc=c.split(",")
for i in range(len(cc)):
    cc[i]=int(cc[i])
# accpted matrix elemets 
a11=aa[0]
a12=aa[1]
a13=aa[2]

a21=bb[0]
a22=bb[1]
a23=bb[2]

a31=cc[0]
a32=cc[1]
a33=cc[2]

l=[[a11,a12,a13,1,0,0],[a21,a22,a23,0,1,0],[a31,a32,a33,0,0,1]]
import pandas as pd
df=pd.DataFrame(l)
# 1 R1-r1/a11
df.loc[0]=df.loc[0]/df.loc[0][0]
# 2 r2--- r2-a21r1
df.loc[1]=df.loc[1]-(df.loc[1][0]*df.loc[0])
# 3 r3--- r3-a21r1
df.loc[2]=df.loc[2]-(df.loc[2][0]*df.loc[0])
# 4 r2--r2%a212
df.loc[1]=df.loc[1]/(df.loc[1][1])
# 5 r3--- r3-a32r2
df.loc[2]=df.loc[2]-(df.loc[2][1]*df.loc[1])
# 6 r1--- r1-a12r2
df.loc[0]=df.loc[0]-(df.loc[0][1]*df.loc[1])
# 7 r3--r3%a13
df.loc[2]=df.loc[2]/(df.loc[2][2])
# 8 r1--- r1-a13r3
df.loc[0]=df.loc[0]-(df.loc[0][2]*df.loc[2])
# 9 r2--- r2-a23r3
df.loc[1]=df.loc[1]-(df.loc[1][2]*df.loc[2])
inverse=df[[3,4,5]]
print()
print('inverse of the Matrix is :-  ')
inverse


# In[ ]:




