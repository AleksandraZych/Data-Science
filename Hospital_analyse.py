import sys
import numpy as np
import pandas as pd

data = pd.read_csv("C:/Users/cp24/Desktop/Nowa_analiza/Hospital.csv")
hospital_types = []
hospital_types.extend(list(data['Hospital Type']))
hospital_types = list(dict.fromkeys(hospital_types))
print(hospital_types)

# making statistic in df object

columns_names = ['Facility Name']
columns_names.extend(hospital_types)

def statistics(data):
    li=[]
    for t in hospital_types[:4]:
        cur=(data[data['Hospital Type'] == t])
        li.extend((cur[['Hospital Type']].count()))

    return li, hospital_types
print(statistics(data))