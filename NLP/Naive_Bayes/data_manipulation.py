import numpy as np
def get_pos():
    t_pos = open("NLP\\Naive_Bayes\\data_pos.txt", "r").readlines()
    return [thing.replace("\n", "") for thing in t_pos]

def get_neg():
    t_neg = open("NLP\\Naive_Bayes\\data_neg.txt", "r").readlines()
    return [thing.replace("\n", "") for thing in t_neg]

def getFreq(x):
    # P(w | class) = w + 1 / Nclass + Vclass
    # w is word freq. N is occurences of that class (sum of all freqs), V is the number of different pos words
    return ((np.array(x)+1) / (sum(x) + len(x)))