import pandas as pd

case_study = pd.read_csv("Soft Skillet_ October Data Live - Activity Data vOct.csv")

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


no_interest_count, engaged_count, deferred_count = ai_seating_metrics_owner(case_study)
print('Owner')
print(f"No Interest: {no_interest_count}")
print(f"Engaged: {engaged_count}")
print(f"Deferred to Other: {deferred_count}")

print('Manager')
no_interest_count, engaged_count, deferred_count = ai_seating_metrics_manager(case_study)
print(f"No Interest: {no_interest_count}")
print(f"Engaged: {engaged_count}")
print(f"Deferred to Other: {deferred_count}")
