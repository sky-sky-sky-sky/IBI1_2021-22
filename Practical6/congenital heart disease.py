import numpy as np
import matplotlib.pyplot as plt

risk={'30':'1.03','35':'1.07','40':'1.11','45':'1.17','50':'1.23','55':'1.32',
    '60':'1.42','65':'1.55','70':'1.72','75':'1.94'}#the dictionary of risk
N = 10
paternal_age=[30,35,40,45,50,55,60,65,70,75]
chd=[1.03,1.07,1.11,1.17,1.23,1.32,1.42,1.55,1.72,1.94]
plt.scatter(paternal_age,chd) #make a picture
plt.show()#show the picture
print('please enter your father/s age')
age=input()#get age
print('the relative risk of congenital hear disease for your father is',risk[age])#let people know the risk of thier father to get congenital hear disease
