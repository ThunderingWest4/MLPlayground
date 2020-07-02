import numpy as np
import data_manipulation as datman #like batman but not

pos_dat = datman.get_pos()
neg_dat = datman.get_neg()
size = len(pos_dat)

#made sure that the two datasets are 'matched' or even; 10 entries in each, 20 total
v_pos = {}
v_neg = {}
#separate vocabularies for positive and negative entries

for i in range(size):
    for word in pos_dat[i].split(" "):
        if(word in v_pos):
            v_pos[word] += 1
        else:
            v_pos[word] = 1
    for word in neg_dat[i].split(" "):
        if(word in v_neg):
            v_neg[word] += 1
        else:
            v_neg[word] = 1

print(v_pos)
print(v_neg)
#now to merge them into one big array

words = []

for x in v_pos.keys():
    if not(x in words):
        words.append(x)
for x in v_neg.keys():
    if not(x in words):
        words.append(x)

#complete vocabulary woo!
#now to get complete counts

for obj in words:
    if not(obj in v_pos.keys()):
        #basically if this word is only negative
        v_pos[obj] = 0
    #same for neg stuff but reverse
    if not(obj in v_neg.keys()):
        #basically if this word is only positive
        v_neg[obj] = 0


complete_voc = [
    words, #vocabulary
    [v_pos[i] for i in words], #pos freqs
    [v_neg[i] for i in words] #neg freqs
]
print(complete_voc)