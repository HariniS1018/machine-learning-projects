# Import libraries
import pandas as pd # For uploading data
import matplotlib.pyplot as plt # For plotting graphs

# Choose dataset file from local directory
from google.colab import files # Uploading data file in google colab
uploaded = files.upload()

# Load Dataset
df = pd.read_csv('mobile_price_range_data.csv')
print(df)
df2 = df.copy()

# summarizing data
df.shape
df.head(5)

# Handling Null values
df.isnull().sum()

# Handling Duplicates
df.duplicated().sum()

# Segregating the data into x and y
x = df.drop('price_range',axis = 1) # Independent Variable or Input
print(x.head(5))
print(type(x))
y = df['price_range'] # Dependent Variable or output
print(y)
print(type(y))

# splitting dataset into train and test
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.25,random_state = 0)
x2 = x_train.copy()

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train) # to avoid bias, fitting the whole dataset to same range of values
x_test = sc.transform(x_test)
print(type(x_train))

# Evaluating classification_report and model score
from sklearn.metrics import confusion_matrix, classification_report

def eval_model(ytest,ypred): # evaluate confusion matrix and classification_report
cm = confusion_matrix(ytest,ypred)
print('\nconfusion matrix:\n', cm)
print(classification_report(ytest,ypred))

def mscore(model): # training and testing score to know how good the model works
print('Train Score',model.score(x_train,y_train))
print('Test Score',model.score(x_test,y_test))

# 1. Applying Logistic Regression
from sklearn.linear_model import LogisticRegression
m1 = LogisticRegression()     # applying and storing the model in variable 'm1'
m1.fit(x_train,y_train)       # train the model with the training data
mscore(m1)                    # calling the function (calculate how good the model works)
ypred_m1 = m1.predict(x_test) # predicting with the test data
print('\npredicted price range for test data:\n',ypred_m1)
eval_model(y_test,ypred_m1)   # calling the function to report the confusion matrix and the model's accuracy

# 2. Applying KNN Model
from sklearn.neighbors import KNeighborsClassifier
m2 = KNeighborsClassifier(n_neighbors = 125, weights = 'distance', p = 1.1, algorithm = 'brute') # applying and storing the model in variable 'm2'
m2.fit(x_train,y_train)       # train the model with the training data
mscore(m2)                    # calling the function (calculate how good the model works)
ypred_m2 = m2.predict(x_test) # predicting with the test data
print('\npredicted price range for test data:\n',ypred_m2)
eval_model(y_test,ypred_m2)   # calling the function to report the confusion matrix and the model's accuracy

# 3. Applying SVM Classifier with linear and rbf kernel
from sklearn.svm import SVC
m3lin = SVC(kernel = 'linear', C = 10) # applying and storing the model in variable 'm3lin'
m3lin.fit(x_train,y_train) # train the model with the training data
mscore(m3lin) # calling the function (calculate how good the model works)
ypred_m3lin = m3lin.predict(x_test)
print('\npredicted price range for test data:\n',ypred_m3lin)
eval_model(y_test,ypred_m3lin) # calling the function to report the confusion matrix and the model's accuracy

m3rbf = SVC(kernel = 'rbf', C = 5, gamma = 0.01) # applying and storing the model in variable 'm3rbf'
m3rbf.fit(x_train,y_train) # train the model with the training data
mscore(m3rbf) # calling the function (calculate how good the model works)
ypred_m3rbf = m3rbf.predict(x_test) # predicting with the test data
print('\npredicted price range for test data:\n',ypred_m3rbf)
eval_model(y_test,ypred_m3rbf) # calling the function to report the confusion matrix and the model's accuracy

# 4. Applying Desicion Tree Model
from sklearn.tree import DecisionTreeClassifier
m4 = DecisionTreeClassifier(criterion = 'entropy', random_state = 0, splitter = 'best') # applying and storing the model in variable 'm4'
m4.fit(x_train,y_train) # train the model with the training data
mscore(m4) # calling the function (calculate how good the model works)
ypred_m4 = m4.predict(x_test) # predicting with the test data
print('\npredicted price range for test data:\n',ypred_m4)
eval_model(y_test,ypred_m4) # calling the function to report the confusion matrix and the model's accuracy
fn = x2.columns
cn = ['0','1','2','3']
from sklearn.tree import plot_tree
plot_tree(m4,feature_names = fn, class_names = cn, filled = True)
plt.show()

# 5. Applying Random Forest
from sklearn.ensemble import RandomForestClassifier
m5 = RandomForestClassifier(n_estimators = 5, criterion = 'entropy', max_depth = 16) # applying and storing the model in variable 'm5'
m5.fit(x_train,y_train) # train the model with the training data
mscore(m5) # calling the function (calculate how good the model works)
ypred_m5 = m5.predict(x_test) # predicting with the test data
print('\npredicted price range for test data:\n',ypred_m5)
eval_model(y_test,ypred_m5)
