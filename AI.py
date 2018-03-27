import xlrd
import csv
import pandas


filename = "Spreadsheet.csv"
names = ["league", "Date", "Blue Team", "Red Team", "FTBT", "FTRT", "FTR", "GBT", "GRT", "KBT", "KRT", "WBT","WRT","TDBT","TDRT","FBBT","FBRT","CWBT","CWRT","DBT","DRT","BBT","BRT","RBT","RRT","TBT","TRT","IBT","IRT"]

data = pandas.read_csv(filename names=names)

print(data.shape)
