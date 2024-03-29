#!/usr/bin/env python3
"""
Main file to run all 4 classifiers

Running command:
$ python NaiveBayesClassifer.py training_pos.txt training_neg.txt test_pos_private.txt test_neg_private.txt
$ python NaiveBayesClassifier.py ../data/training_pos.txt ../data/training_neg.txt ../data/test_pos_public.txt ../data/test_neg_public.txt

"""
import sys

from mnb_bow import *
from mnb_tfidf import *
from gnb_bow import *
from gnb_tfidf import *

def main(filenames):
    results = {'ACCURACY MEASURE: TP, FN, FP, TN': [0,0,0,0]}

    pos, neg, numReviews, occurPos, occurNeg = train_prep(filenames)

    gnb_bow = GNB_BOW(pos, neg, numReviews)
    gnb_bow.train()
    TP, FN, FP, TN = gnb_bow.test(filenames)
    results['gnb_bow'] = [TP, FN, FP, TN]

    gnb_tfidf = GNB_TFIDF(pos, neg, numReviews, occurPos, occurNeg)
    gnb_tfidf.train()
    TP, FN, FP, TN = gnb_tfidf.test(filenames)
    results['gnb_tfidf'] = [TP, FN, FP, TN]

    mnb_bow = MNB_BOW(pos, neg)
    mnb_bow.train()
    TP, FN, FP, TN = mnb_bow.test(filenames)
    results['mnb_bow'] = [TP, FN, FP, TN]

    mnb_tfidf = MNB_TFIDF(pos, neg, occurPos, occurNeg, numReviews)
    mnb_tfidf.train()
    TP, FN, FP, TN = mnb_tfidf.test(filenames)
    results['mnb_tfidf'] = [TP, FN, FP, TN]

    print(results)

if __name__ == "__main__":
    filenames = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]]
    main(filenames)
