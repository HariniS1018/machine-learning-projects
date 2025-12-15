import pandas as pd                 # For uploading data
import matplotlib.pyplot as plt     # For plotting graphs

from google.colab import files      # Uploading data file in google colab
uploaded = files.upload()

df = pd.read_csv('amazon_alexa (1).csv')                # Loading dataset
#print(df)

df.shape                            # no. of rows and columns in dataset
#df.head(5)

df.isnull().sum()                   # handling null values

df.duplicated().sum()

df['feedback'].value_counts()      # total no. of positive and negative sentiments

import re
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

import nltk
nltk.download('stopwords')

sw = stopwords.words('english')
lm = WordNetLemmatizer()

nltk.download('wordnet')

nltk.download('omw-1.4')

nltk.download('punkt')

msg = []
for i in text:
  t = i.lower()                       # words to lowercase
  t = re.sub('[^A-Za-z0-9]',' ',t)    # punctuation removal
  t = word_tokenize(t)                # tokenization
  t = [i for i in t if i not in sw]   # removing stopwords
  t = [lm.lemmatize(i) for i in t]    # Lemmatization
  t = " ".join(t)                     # list of sentences after all preprocessing(optional)
  msg.append(t)
#print(msg)

x = msg
y = df['feedback']

# Transform the words into vectors using Count Vectorizer

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
cv.fit(msg)

sm1 = cv.transform(x).toarray()
sm2 = cv.get_feature_names_out()
print(sm2)

# Splitting data into training and test data

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(sm1,y,test_size = 0.25,random_state = 0)

#Evaluating classification_report and model score

from sklearn.metrics import confusion_matrix, classification_report

def eval_model(ytest,ypred):                          # evaluate confusion matrix and classification_report
  cm = confusion_matrix(ytest,ypred)
  print('\nconfusion matrix:\n', cm)
  print(classification_report(ytest,ypred))
  #print('Accuracy Score:', accuracy_score(ytest,ypred)) # display accuracy score of the model

def mscore(model):                                    # training and testing score to know how good the model works
  print('Train Score',model.score(x_train,y_train))
  print('Test Score',model.score(x_test,y_test))

# Applying Multinomial Naïve Bayes Classification

from sklearn.naive_bayes import MultinomialNB

mnb1 = MultinomialNB()
mnb1.fit(x_train,y_train)
mscore(mnb1)

ypred_mnb = mnb1.predict(x_test)
print('\npredicted price range for test data:\n', ypred_mnb)

eval_model(y_test,ypred_mnb)

# Applying Logistic Regression

from sklearn.linear_model import LogisticRegression

m1 = LogisticRegression()         
m1.fit(x_train,y_train)           
mscore(m1)                        

ypred_m1 = m1.predict(x_test)     
print('\npredicted price range for test data:\n',ypred_m1)

eval_model(y_test,ypred_m1)

# Applying KNN Classification

from sklearn.neighbors import KNeighborsClassifier

m2 = KNeighborsClassifier(n_neighbors = 5)
m2.fit(x_train,y_train)
mscore(m2)

ypred_m2 = m2.predict(x_test)
print('\npredicted price range for test data:\n',ypred_m2)

eval_model(y_test,ypred_m2)