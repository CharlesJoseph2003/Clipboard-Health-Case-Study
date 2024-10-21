import pandas as pd

case_study = pd.read_csv("Soft Skillet_ October Data Live - Activity Data vOct.csv")

def smooth_seating_metrics(df): 
    smooth_no_interest = df[(df["Pitch"] == "Smooth") & (df["Disposition"] == "No Interest")]
    smooth_engaged = df[(df["Pitch"] == "Smooth") & (df["Disposition"] == "Engaged")]
    smooth_deferred = df[(df["Pitch"] == "Smooth") & (df["Disposition"] == "Deferred to Other Stakeholder")]

    no_interest_count = smooth_no_interest.shape[0]
    engaged_count = smooth_engaged.shape[0]
    deferred_count = smooth_deferred.shape[0]
    return no_interest_count, engaged_count, deferred_count


def smooth_seating_metrics_owner(df):
    smooth_owner_no_interest = df[(df["Pitch"] == "Smooth") & (df["Person"] == "Owner") & (df["Disposition"] == "No Interest")]
    smooth_owner_engaged = df[(df["Pitch"] == "Smooth") & (df["Person"] == "Owner") & (df["Disposition"] == "Engaged")]
    smooth_owner_deferred = df[(df["Pitch"] == "Smooth") & (df["Person"] == "Owner") & (df["Disposition"] == "Deferred to Other Stakeholder")]

    no_interest_count = smooth_owner_no_interest.shape[0]
    engaged_count = smooth_owner_engaged.shape[0]
    deferred_count = smooth_owner_deferred.shape[0]
    return no_interest_count, engaged_count, deferred_count


def smooth_seating_metrics_manager(df):
    smooth_manager_no_interest = df[(df["Pitch"] == "Smooth") & (df["Person"] == "Manager") & (df["Disposition"] == "No Interest")]
    smooth_manager_engaged = df[(df["Pitch"] == "Smooth") & (df["Person"] == "Manager") & (df["Disposition"] == "Engaged")]
    smooth_manager_deferred = df[(df["Pitch"] == "Smooth") & (df["Person"] == "Manager") & (df["Disposition"] == "Deferred to Other Stakeholder")]

    no_interest_count = smooth_manager_no_interest.shape[0]
    engaged_count = smooth_manager_engaged.shape[0]
    deferred_count = smooth_manager_deferred.shape[0]
    return no_interest_count, engaged_count, deferred_count


no_interest_count, engaged_count, deferred_count = smooth_seating_metrics_owner(case_study)
print(f"No Interest: {no_interest_count}")
print(f"Engaged: {engaged_count}")
print(f"Deferred to Other: {deferred_count}")


no_interest_count, engaged_count, deferred_count = smooth_seating_metrics_manager(case_study)
print(f"No Interest: {no_interest_count}")
print(f"Engaged: {engaged_count}")
print(f"Deferred to Other: {deferred_count}")
