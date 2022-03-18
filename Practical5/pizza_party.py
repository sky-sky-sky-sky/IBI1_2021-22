e=1 # if we do not cut, we have 1 piece of pizza
n=0 # how many cut we need
while e<=64:
	n=n+1
	e=(n*n+n+2)/2
print('at least cut',n,'we have',e,' piece of pizza') 
