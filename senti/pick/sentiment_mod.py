import nltk
import random
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize




class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)

        choice_votes = votes.count(mode(votes))
        conf = float(choice_votes) / len(votes)
        return conf

import os
dir_name = os.path.dirname(os.path.abspath(__file__))

documents_f = open(dir_name + "/documents.pickle", "rb")
documents = pickle.load(documents_f)
documents_f.close()




word_features5k_f = open(dir_name + "/word_features5k.pickle", "rb")
word_features = pickle.load(word_features5k_f)
word_features5k_f.close()


def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features



featuresets_f = open(dir_name + "/featuresets.pickle", "rb")
featuresets = pickle.load(featuresets_f)
featuresets_f.close()

random.shuffle(featuresets)
print(len(featuresets))



testing_set = featuresets[16500:]
training_set = featuresets[:16500]




open_file = open(dir_name + "/originalnaivebayes5k.pickle", "rb")
classifier = pickle.load(open_file)
open_file.close()


open_file = open(dir_name + "/MNB_classifier5k.pickle", "rb")
MNB_classifier = pickle.load(open_file)
open_file.close()



open_file = open(dir_name + "/BernoulliNB_classifier5k.pickle", "rb")
BernoulliNB_classifier = pickle.load(open_file)
open_file.close()


open_file = open(dir_name + "/LogisticRegression_classifier5k.pickle", "rb")
LogisticRegression_classifier = pickle.load(open_file)
open_file.close()


open_file = open(dir_name + "/LinearSVC_classifier5k.pickle", "rb")
LinearSVC_classifier = pickle.load(open_file)
open_file.close()


open_file = open(dir_name + "/SGDC_classifier5k.pickle", "rb")
SGDC_classifier = pickle.load(open_file)
open_file.close()

linearsvc = nltk.classify.accuracy(LinearSVC_classifier, testing_set)*100
basic_classifier = nltk.classify.accuracy(classifier, testing_set)*100
sdgc = nltk.classify.accuracy(SGDC_classifier, testing_set)*100
mnb = nltk.classify.accuracy(MNB_classifier, testing_set)*100
bernoulli = nltk.classify.accuracy(BernoulliNB_classifier, testing_set)*100
logisticreg = nltk.classify.accuracy(LogisticRegression_classifier, testing_set)*100

avg_accuracy = (linearsvc+basic_classifier+sdgc+mnb+bernoulli+logisticreg)/6

print("Original Naive Bayes Algo accuracy percent:", basic_classifier)
print("MNB_classifier accuracy percent:", mnb)
print("BernoulliNB_classifier accuracy percent:", bernoulli)
print("LogisticRegression_classifier accuracy percent:", logisticreg)
print("LinearSVC_classifier accuracy percent:", linearsvc)
print("SGDClassifier accuracy percent:",sdgc)


voted_classifier = VoteClassifier(
                                  classifier,
                                  LinearSVC_classifier,
                                  MNB_classifier,
                                  BernoulliNB_classifier,
                                  LogisticRegression_classifier,
                                  SGDC_classifier)


def sentiment(text,score):
    feats = find_features(text)
    classify_tag = voted_classifier.classify(feats)
    classify_confidence = voted_classifier.confidence(feats)
    if classify_tag == 'pos':
        dscore = (score + (classify_confidence*avg_accuracy)/2)
    if classify_tag == 'neg':
        dscore = (score - (classify_confidence*avg_accuracy)/2)
    ascore = score - (classify_confidence*avg_accuracy)
    if ascore > 1:
        atag = 'True'
    return dscore,atag
