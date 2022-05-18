def seq(t):
    n1=0
    n2=0
    n3=0
    n4=0
    s=t.upper()#upper words
    sequence=list(s)
    for i in range(len(sequence)):#Calculate percentage
        if sequence[i]=='T':
            n1=n1+1
        elif sequence[i]=='A':
            n2=n2+1
        elif sequence[i]=='G':
            n3=n3+1 
        elif sequence[i]=='C':
            n4=n4+1 
    print('percentage of T is',n1/len(sequence),'percentage of A is',n2/len(sequence),'percentage of G is',n3/len(sequence),'percentage of C is',n4/len(sequence))
seq('AGCTGatcgtGATGCTgatcgTGATCGTagtACGTAgtcgtAGTCGTgatgtcgtagctgactGATGTgtgctagCGTAgtcgtAGCTG')# this is the input sequence
print('this is a example, please input your sequence')
a=input()
seq(a)