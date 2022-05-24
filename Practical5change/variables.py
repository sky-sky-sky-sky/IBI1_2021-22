#this date means 7 March.

from turtle import Turtle


a=19245301 #there	 had been	 a total 19,245,301 cases of COVID-19 in the UK since the pandemic began.
b=4218520  #On this date in 2021 there had been a total of 4,218,520 cases.
c=271           #On this date in 2020 there had been 271 cases.
d=b-c          #Calculate the difference between the numbers of cases in 2020 and 2021.
e=a-b          #Calculate the difference between the numbers of cases in 2021 and 2022.
if d>e:
	print('d is greater')
if e>d:
	print('e is greater')

X=True
Y=False
W=X and Y
print(W)
