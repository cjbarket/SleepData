import numpy as np
import pandas as pd

aug = pd.read_csv("EditedCSVfiles/AUGUSTsleep.csv", index_col = 0)
sep = pd.read_csv("EditedCSVfiles/SEPTEMBERsleep.csv", index_col = 0)
oc = pd.read_csv("EditedCSVfiles/OCTOBERsleep.csv", index_col = 0)
nov = pd.read_csv("EditedCSVfiles/NOVEMBERsleep.csv", index_col = 0)
dec = pd.read_csv("EditedCSVfiles/EarlyDECsleep.csv", index_col = 0)
rest = pd.read_csv("EditedCSVfiles/(22-12-07)TO(23-01-06)Sleep.csv", index_col = 0)

completeDF = pd.concat([rest,dec,nov,oc,sep,aug], axis = 0)
completeDF.to_csv("EditedCSVfiles/CompleteSets/CompleteSleep.csv")
