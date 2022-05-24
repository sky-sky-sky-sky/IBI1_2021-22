from xml.dom.minidom import parse 
import xml.dom.minidom
import matplotlib.pyplot as plt
import numpy as np

DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
term_list=collection.getElementsByTagName("term")
print("There are ",len(term_list)," terms in the file.")

data={}
childnode={}
def function(term,e):
    child_list=data[term]
    for child in child_list:
        if childnode[child]=={child:0}:
            e.append(child)
            for i in e:
                childnode[i][child] = 0
            function(child,e)
            del e[-1]
        else:
            for i in e:
                childnode[i].update(childnode[child])


for term in term_list:
    id=term.getElementsByTagName('id')[0].childNodes[0].data
    data[id]=[]
    childnode[id]={id:0}

translation=[]
for term in term_list:
    name=term.getElementsByTagName('id')[0].childNodes[0].data
    trunk_list=term.getElementsByTagName('is_a')
    for trunk in trunk_list:
        data[trunk.childNodes[0].data].append(name)
    if 'translation' in term.getElementsByTagName('defstr')[0].childNodes[0].data.lower():
        translation.append(name)

data1=[]
data2=[]
n=data.keys()
for i in n:
    e=[i]
    function(i,e)
    data1.append(len(childnode[i].keys())-1)
    if i in translation:
        data2.append(len(childnode[i].keys())-1)    

plt.boxplot(data1)
plt.title('childnode number of all GO terms')
plt.xlabel("all GO terms")
plt.ylabel("Number")
plt.show()

plt.boxplot(data2)
plt.title('childnode number of terms associated with translation')
plt.xlabel("associated with translation")
plt.ylabel("Number")
plt.show()

print("The average of childnodes of all terms",np.average(data1))
print("The average of childnodes of terms associated with translation",np.average(data2))
if np.average(data1)<np.average(data2):
    print('The average of child nodes associated with translationis bigger than that of overall terms.')
elif np.average(data1)==np.average(data2):
    print('there is no different')
elif np.average(data1)>np.average(data2):
    print('The average of child nodes associated with translationis smaller than that of overall terms.')













