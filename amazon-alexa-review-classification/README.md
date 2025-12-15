# Classification-AmazonAlexaReviews

### Project Description:
Problem statement: Create a classification model to predict the sentiment either (1 or 0) based on Amazon Alexa reviews.  
Context: This dataset consists of a nearly 3000 Amazon customer reviews (input text), star ratings, date of review, variant and feedback of 
various amazon Alexa products like Alexa Echo, Echo dots, Alexa Firesticks etc. for learning how to train Machine for sentiment analysis.

### Details of features:
The columns are described as follows:
  1) rating: Product rating
  2) Date: date on which the product was rated
  3) variation: variation of the product
  4) verfified_reviews: the verified reviews for the alexa
  5) feedback: 1(Positive) or 0 (Negative)

### Steps to consider:
  1) Read the dataset
  2) Handle null values, and duplicates.
  3) check class balance.
  4) Rename columns and set index.
  5) check data type of each feature and convert accordingly.
  6) Preprocess the Amazon Alexa reviews based on the following parameter:  
    a) Tokenizing words  
    b) Convert words to lower case  
    c) Removing Punctuations  
    d) Removing Stop words  
    e) Stemming or lemmatizing the words  
    f) Transform the words into vectors using Count Vectorizer OR  TF-IDF Vectorizer  
  7) Split data into training and test data.
  8) Apply the following models on the training dataset and generate the predicted value for the test dataset  
    a) Multinomial Naïve Bayes Classifier
    b) Logistic Regression  
    c) KNN Classifier
    d) Decision Tree Classifier
  7) Predict the feedback for test data
  8) Compute classification report for each of these models
  9) Report the model with the best accuracy
