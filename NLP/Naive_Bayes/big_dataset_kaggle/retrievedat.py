import csv
import os
# make sure that we're in right directory to access the csv file
def retcsv():
    print("Reading Data in. . . ")
    result = []
    path = "NLP\\Naive_Bayes\\big_dataset_kaggle\\16mil_kaggle_dataset.csv"

    with open(path) as csvfile:
        csvreader=csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            result.append(row)

    return result
