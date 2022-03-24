from turtle import width
import numpy as np
import matplotlib.pyplot as plt

N = 8
marks=[45,36,86,57,53,92,65,45]
marks.sort()
print(marks)
pl = plt.boxplot(marks) 

plt.show()

n=(45+36+86+57+53+92+65+45)/8
if n>=60:
    print('yes, this is higher than the pass mark of 60%')
if n<60:
    print('no,this is not higher than the pass mark of 60%')