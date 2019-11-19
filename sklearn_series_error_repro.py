from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB


# still haven't seen this script work

# i grabbed a random book from the Esperanto text corpus
# https://tekstaro.com/
text_process = open('vojagho-al-kazohinio.xml').read()

# PROBLEM: don't know what messages{} is supposed to look like

messages = { 'messages': ['Estus agrable trovi solvon', 'jen hazarda frazo'],
             'label': ['thiago', 'naomi']
           }

bow_transformer = CountVectorizer(analyzer=text_process).fit(messages['message'])

msg_train, msg_test, label_train, label_test = train_test_split(messages['message'], messages['label'], test_size=0.2)

pipeline = Pipeline([
    ('bow', CountVectorizer(analyzer=text_process)),  # strings to token 
    ('tfidf', TfidfTransformer()),  # integer counts to weighted TF-IDF scores
    ('classifier', MultinomialNB()),  # train on TF-IDF vectors w/ Naive Bayes 
])

NB_Classifier = pipeline.fit(msg_train,label_train)

