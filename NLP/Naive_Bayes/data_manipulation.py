def get_pos():
    t_pos = open("NLP\\Naive_Bayes\\data_pos.txt", "r").readlines()
    return [thing.replace("\n", "") for thing in t_pos]

def get_neg():
    t_neg = open("NLP\\Naive_Bayes\\data_neg.txt", "r").readlines()
    return [thing.replace("\n", "") for thing in t_neg]