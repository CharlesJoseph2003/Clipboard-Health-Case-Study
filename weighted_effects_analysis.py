import pandas as pd

def weighted_effects():
    df = pd.read_csv("Soft Skillet_ October Data Live - Activity Data vOct.csv")
    new_df = df[(df["Pitch"] == "AI") | (df["Pitch"] == "Operator") | (df["Pitch"]=="Smooth")]

    weights = {
        'Engaged':3,
        'Deferred to Other Stakeholder':1,
        'No Interest':0
    }

    new_df['Disposition Score'] = new_df['Disposition'].map(weights)
    grouped = new_df.groupby('Pitch')['Disposition Score'].mean().reset_index()

    grouped = grouped.sort_values(by='Disposition Score', ascending=False)
    return grouped

def weighed_effects_persons():
    df = pd.read_csv("Soft Skillet_ October Data Live - Activity Data vOct.csv")
    new_df = df[(df["Pitch"] == "AI") | (df["Pitch"] == "Operator") | (df["Pitch"]=="Smooth")]

    weights = {
        'Engagenew_dfd':3,
        'Deferred to Other Stakeholder':1,
        'No Interest':0
    }
    person_weight = {
    'Owner': 2,  
    'Manager': 1.0
}
    new_df['Disposition Score'] = new_df['Disposition'].map(weights)
    new_df['Person Weight'] = new_df['Person'].map(person_weight)

    new_df['Weighted Disposition Score'] = new_df['Disposition Score'] * new_df['Person Weight']

    grouped = new_df.groupby('Pitch')['Weighted Disposition Score'].mean().reset_index()

    grouped = grouped.sort_values(by='Weighted Disposition Score', ascending=False)
    return grouped


weighted_normal = weighted_effects()
print(weighted_normal)
manager_owner_effects = weighed_effects_persons()
print(manager_owner_effects)
