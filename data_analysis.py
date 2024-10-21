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


def ai_seating_metrics(df): 
    ai_no_interest = df[(df["Pitch"] == "AI") & (df["Disposition"] == "No Interest")]
    ai_engaged = df[(df["Pitch"] == "AI") & (df["Disposition"] == "Engaged")]
    ai_deferred = df[(df["Pitch"] == "AI") & (df["Disposition"] == "Deferred to Other Stakeholder")]

    no_interest_count = ai_no_interest.shape[0]
    engaged_count = ai_engaged.shape[0]
    deferred_count = ai_deferred.shape[0]
    return no_interest_count, engaged_count, deferred_count


def ai_seating_metrics_owner(df):
    ai_owner_no_interest = df[(df["Pitch"] == "AI") & (df["Person"] == "Owner") & (df["Disposition"] == "No Interest")]
    ai_owner_engaged = df[(df["Pitch"] == "AI") & (df["Person"] == "Owner") & (df["Disposition"] == "Engaged")]
    ai_owner_deferred = df[(df["Pitch"] == "AI") & (df["Person"] == "Owner") & (df["Disposition"] == "Deferred to Other Stakeholder")]

    no_interest_count = ai_owner_no_interest.shape[0]
    engaged_count = ai_owner_engaged.shape[0]
    deferred_count = ai_owner_deferred.shape[0]
    return no_interest_count, engaged_count, deferred_count


def ai_seating_metrics_manager(df):
    ai_manager_no_interest = df[(df["Pitch"] == "AI") & (df["Person"] == "Manager") & (df["Disposition"] == "No Interest")]
    ai_manager_engaged = df[(df["Pitch"] == "AI") & (df["Person"] == "Manager") & (df["Disposition"] == "Engaged")]
    ai_manager_deferred = df[(df["Pitch"] == "AI") & (df["Person"] == "Manager") & (df["Disposition"] == "Deferred to Other Stakeholder")]

    no_interest_count = ai_manager_no_interest.shape[0]
    engaged_count = ai_manager_engaged.shape[0]
    deferred_count = ai_manager_deferred.shape[0]
    return no_interest_count, engaged_count, deferred_count


no_answer = no_answer_frequency(case_study)
print(no_answer)

answer = answer_frequency(case_study)
print(answer)

no_interest_count, engaged_count, deferred_count = ai_seating_metrics_owner(case_study)
print(f"No Interest: {no_interest_count}")
print(f"Engaged: {engaged_count}")
print(f"Deferred to Other: {deferred_count}")
