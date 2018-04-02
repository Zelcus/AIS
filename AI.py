import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
data = pd.read_csv("Test.txt")
print (data.head())


'''
names = ["league", "Date", "Blue Team", "Red Team", "FTBT", "FTRT", "FTR", "GBT", "GRT", "KBT", "KRT", "WBT","WRT","TDBT","TDRT","FBBT","FBRT","CWBT","CWRT","DBT","DRT","BBT","BRT","RBT","RRT","TBT","TRT","IBT","IRT"]

data = pandas.read_csv(filename, names=names)
'''

y = data.FTR
X = data.drop("FTR", axis = 1)


#test_size = the amount of test-cases we would like.
'''
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2)




print()
print ("\nX_train:\n")
print(X_train.head())

print ("\nX_test:\n")
print(X_test.head())
'''

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)
print (clf.predict([[1, 3]]))


