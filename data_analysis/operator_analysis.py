import pandas as pd

case_study = pd.read_csv("Soft Skillet_ October Data Live - Activity Data vOct.csv")

def operator_metrics(df): 
    operator_no_interest = df[(df["Pitch"] == "Operator") & (df["Disposition"] == "No Interest")]
    operator_engaged = df[(df["Pitch"] == "Operator") & (df["Disposition"] == "Engaged")]
    operator_deferred = df[(df["Pitch"] == "Operator") & (df["Disposition"] == "Deferred to Other Stakeholder")]

    no_interest_count = operator_no_interest.shape[0]
    engaged_count = operator_engaged.shape[0]
    deferred_count = operator_deferred.shape[0]
    return no_interest_count, engaged_count, deferred_count


def operator_metrics_owner(df):
    operator_owner_no_interest = df[(df["Pitch"] == "Operator") & (df["Person"] == "Owner") & (df["Disposition"] == "No Interest")]
    operator_owner_engaged = df[(df["Pitch"] == "Operator") & (df["Person"] == "Owner") & (df["Disposition"] == "Engaged")]
    operator_owner_deferred = df[(df["Pitch"] == "Operator") & (df["Person"] == "Owner") & (df["Disposition"] == "Deferred to Other Stakeholder")]

    no_interest_count = operator_owner_no_interest.shape[0]
    engaged_count = operator_owner_engaged.shape[0]
    deferred_count = operator_owner_deferred.shape[0]
    return no_interest_count, engaged_count, deferred_count


def operator_metrics_manager(df):
    operator_manager_no_interest = df[(df["Pitch"] == "Operator") & (df["Person"] == "Manager") & (df["Disposition"] == "No Interest")]
    operator_manager_engaged = df[(df["Pitch"] == "Operator") & (df["Person"] == "Manager") & (df["Disposition"] == "Engaged")]
    operator_manager_deferred = df[(df["Pitch"] == "Operator") & (df["Person"] == "Manager") & (df["Disposition"] == "Deferred to Other Stakeholder")]

    no_interest_count = operator_manager_no_interest.shape[0]
    engaged_count = operator_manager_engaged.shape[0]
    deferred_count = operator_manager_deferred.shape[0]
    return no_interest_count, engaged_count, deferred_count


