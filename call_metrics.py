import pandas as pd

case_study = pd.read_csv("Soft Skillet_ October Data Live - Activity Data vOct.csv")

def no_answer_frequency(df):
    counter = 0
    for i in df["Call Connect"]:
        if i == "No Answer":
            counter+=1
    return counter

def answer_frequency(df):
    counter = 0
    for i in df["Call Connect"]:
        if i == "Connected":
            counter+=1
    return counter

def owner_frequency(df):
    counter = 0
    for i in df["Person"]:
        if i == "Owner":
            counter+=1
    return counter

def manager_frequency(df):
    counter = 0
    for i in df["Person"]:
        if i == "Manager":
            counter+=1
    return counter


no_answer = no_answer_frequency(case_study)
print(no_answer)

answer = answer_frequency(case_study)
print(answer)