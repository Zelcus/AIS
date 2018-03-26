import xlrd
import pandas as pd
import xgboost as xgb
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from IPython.display import display

data = pd.read_csv("final_dataset.csv")

display(data.head())


