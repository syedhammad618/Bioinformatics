
seq = open('test1.txt', 'r')
import itertools

chains=[]
[chains.append(line[:-1]) for line in seq]

# motif_name=input('Enter Motif name: ')
s='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
t=list(itertools.combinations(s,2))
list1=[]
list2=[]
list3=[]
for i in t:
    w=''.join(i)
    word1="S{0}K".format(w)
    list1.append(word1)
for i in s:
       word2="S{0}N".format(i)
       word3="Y{0}N".format((i))
       list2.append(word2)
       list3.append(word3)
words=list1+list2+list3

for i,sequence in enumerate(chains):
    
    for word in words:
        idx = sequence.find(word)
        if idx != -1:
            result = "Motif Present in the given Sequence At line  Number {0} Which is: ".format(i+1)
            result += word +', '

            print(result[:-2])          
   