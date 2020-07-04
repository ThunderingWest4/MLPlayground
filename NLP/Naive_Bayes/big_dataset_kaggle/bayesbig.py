import retrievedat as retdat
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import numpy as np

class nlp():

    def __init__(self):
        data = retdat.retcsv()
        print(data[0], data[len(data)-1])
        #Data doesn't appear to have built in columns so here they are:
        # col 1: Sentiment (0=neg, 2-neutral, 4=pos)
        # col 6: actual tweet content
        # these are the only two important ones
        self.ps = PorterStemmer()

        temp = [[(int(data[i][0])/2)-1, data[i][5]] for i in range(len(data))]
        #now we only have the sentiments and tweets and the sentiments are now -1, 0, 1 instead of 0, 2, 4
        #format: [sentiment, tweet]
        self.complete = []
        self.totalposwords = 0
        self.totalnegwords = 0
        for pair in temp:
            if(pair[0]!=0):
                self.complete.append(pair)
                #eliminating all the neutral tweets leaving only pos and neg

    def preprocess(self):
        self.filtered = []
        for pair in self.complete:
            tweet = pair[1].split(" ")
            toadd = []
            for word in tweet:
                #iterate through "words" in tweets
                if((not (tweet[0]=="@" or tweet[0]=="#"))):
                    #if it's not a tag or hashtag
                    toadd.append(self.ps.stem(self.removePunc(word)))
                    #basically quaranteeing that it's an actual word and not a hashtag or user handle
                    #and we turn it into its stem using the Natural Language ToolKit (nltk) 
                    #i.e. happy/happiness/happier -> happi, language/languages -> languag, etc

            #surely there won't be a tweet that's just a hashtag or tagging another user
            #right?
            #i really hope so....
            self.filtered.append([toadd, pair[0]])
    
    def getfreqs(self):
        #purpose is to get frequencies of specific words in different sentiment tweets
        self.fpos = {}
        self.fneg = {}
        for pair in self.filtered:
            #going through tweets with punctuation, spaces, etc removed and turned to roots
            words = pair[0]
            sent = pair[1]
            for wrd in words:
                #sentiment is either 1 or -1
                if(wrd in (fpos if sent==1 else fneg).keys()):
                    (fpos if sent==1 else fneg)[wrd] += 1
                else:
                    (fpos if sent==1 else fneg)[wrd] = 1

                if(sent==1):
                    self.totalposwords += 1 # one more positive word
                else:
                    #sent has to be -1, only other option
                    self.totalnegwords += 1

    def probabilities(self):
        probpos = []
        probneg = []
        words = []
        for w in self.fpos.keys():
            words.append(w)
        for w in self.fpos.keys():
            if not(w in words):
                words.append(w)
        #Equation: (wordOccurences + 1) / (total words of class) + (total different words in class)
        posdenom = self.totalposwords + len(self.probpos.keys())
        negdenom = self.totalnegwords + len(self.probneg.keys())
        for w in words:
            probpos.append((self.fpos[w] + 1)/posdenom)
            probneg.append((self.fneg[w] + 1)/negdenom)
        
        self.compProb = [
            words, 
            probpos, 
            probneg
        ]
        #should all be same dimensions and have all the words

    def lambdas(self):
        logs = []
        for i in range(len(self.compProb)):
            #log(pos / neg)
            logs.append(np.log(self.compProb[1][i] / self.compProb[2][i]))
        self.compProb.append(logs)
        #now compProb has all the words, positive probabilities, negative probabilities, and the overall log/lambda of their probability

    def removePunc(self, s):
        ret = []
        punct = "!@#$%^&*():;,.<>?/\\[]{}`~'+-_="
        for letter in s:
            #assuming that s is a single word
            if not(letter in punct):
                #if it is not a punctuation thing
                ret.append(letter)
        return "".join(ret)


    def analyze(self):
        #method to do the full analysis process
        print("Beginning Data Analysis. . . ")
        print("Pre-processing text. . . ")
        self.preprocess()
        print("Text successfully preprocessed. Computing Frequencies. . . ")
        self.getfreqs()
        print("Frequencies computed. Getting probabilities. . . ")
        self.probabilities()
        print("Lambda time. . . ")
        self.lambdas()
        print("Complete!")
    
tester = nlp()
tester.analyze()

