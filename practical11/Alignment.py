seq_human="MTGVFDRRVPSIRSGDFQAPFQTSAAMHHPSQESPTLPESSATDSDYYSPTGGAPHGYCSPTSASYGKALNPYQYQYHGVNGSAGSYPAKAYADYSYASSYHQYGGAYNRVPSATNQPEKEVTEPEVRMVNGKPKKVRKPRTIYSSFQLAALQRRFQKTQYLALPERAELAASLGLTQTQVKIWFQNKRSKIKKIMKNGEMPPEHSPSSSDPMACNSPQSPAVWEPQGSSRSLSHHPHAHPPTSNQSPASSYLENSASWYTSAASSINSHLPPPGSLQHPLALASGTLY"
seq_mouse="MTGVFDRRVPSIRSGDFQAPFPTSAAMHHPSQESPTLPESSATDSDYYSPAGAAPHGYCSPTSASYGKALNPYQYQYHGVNGSAAGYPAKAYADYGYASPYHQYGGAYNRVPSATSQPEKEVAEPEVRMVNGKPKKVRKPRTIYSSFQLAALQRRFQKTQYLALPERAELAASLGLTQTQVKIWFQNKRSKIKKIMKNGEMPPEHSPSSSDPMACNSPQSPAVWEPQGSSRSLSHHPHAHPPTSNQSPASSYLENSASWYPSAASSINSHLPPPGSLQHPLALASGTLY"
seq_random="GDYHNIYEMQSTDNDVIIVLCESYWQNRYWCGYKQNCIFEDSSLFAPSEVDWAVNGYPPYRAVNMHKYEYDYATPTPQKMMWWHLPIWSWHFWGWNIRTWDILTNSGNTMGFCYCAWVCNLPCMILCHARFAFSTDKKPFSVHTFIIKICHTQPALAVTEPNADSCCMIFPLIGKSYCHTCGTWDFYPNEVKYQFNFSAATQYENVIYIFHHICQDVRRGCTDIELNHFWMSHHVANRKLENIVGYRAILRFIGSKCAQNMRSLFAHPWQSFQDHKEYDWHGNLGLNWP"
b=list(seq_human)
c=list(seq_mouse)
d=list(seq_random)
change={'A':'1','R':'2','N':'3','D':'4','C':'5','Q':'6','E':'7','G':'8','H':'9','I':'10','L':'11','K':'12','M':'13','F':'14','P':'13','S':'16','T':'17','W':'18','Y':'19','V':'20','B':'21','Z':'22','X':'23'}
import openpyxl
a=openpyxl.load_workbook('BLOSUM.xlsx')
sheet=a.active
def different(A,B):
    distance=0
    scores=0
    for i in range(len(A)):
        scores=scores+sheet.cell(row=int(change[A[i]])+1,column=int(change[B[i]])+1).value
        if A[i]!=B[i]:       
            distance=1+distance
            percentage=(len(A)-distance)/len(A)
    print(distance,round(percentage,3),scores)
different(b,c)
different(c,d)
different(d,b)



#


#comparing the edit distance, we can find that the distance between human and mouse is 10, while human to random and mouse to random are 280 and 281 respectively, so human and mouse are very similar comparing to the random.
#comparing the percentage of identical amino acids, we can find that the percentage of identical amino acids human and mouse is 0.965, while human to random and mouse to random are 0.028 and 0.031 respectively, so human and mouse are very similar comparing to the random.
#comparing the scores, we can find thatscores human and mouse is 1429, while human to random and mouse to random are -275 and -264 respectively, so human and mouse are very similar comparing to the random.