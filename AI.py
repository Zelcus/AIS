import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
data = pd.read_csv("Test.txt")


print (data.head())


'''
names = ["league", "Date", "Blue Team", "Red Team", "FTBT", "FTRT", "FTR", "GBT", "GRT", "KBT", "KRT", "WBT","WRT","TDBT","TDRT","FBBT","FBRT","CWBT","CWRT","DBT","DRT","BBT","BRT","RBT","RRT","TBT","TRT","IBT","IRT"]

data = pandas.read_csv(filename, names=names)
'''
#FTR works as our label the rest is our features.
y = data.FTR
X = data.drop("FTR", axis = 1)



#test_size = the amount of test-cases we would like.

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size= .2)



'''
print()
print ("\nX_train:\n")
print(X_train.head())

print ("\nX_test:\n")
print(X_test.head())
'''

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)
#Blue Team with ID X vs Red Team with ID Y.
predictions = clf.predict(X_test)
print(predictions)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, predictions))
