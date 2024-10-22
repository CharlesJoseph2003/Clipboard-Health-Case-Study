import pandas as pd

def weighted_effects():
    df = pd.read_csv("Soft Skillet_ October Data Live - Activity Data vOct.csv")
    
    # Use .loc to modify a slice of the DataFrame
    new_df = df[(df["Pitch"] == "AI") | (df["Pitch"] == "Operator") | (df["Pitch"] == "Smooth")].copy()

    weights = {
        'Engaged': 2,
        'Deferred to Other Stakeholder': 1,
        'No Interest': 0
    }

    # Set the 'Disposition Score' with .loc to avoid SettingWithCopyWarning
    new_df.loc[:, 'Disposition Score'] = new_df['Disposition'].map(weights)
    grouped = new_df.groupby('Pitch')['Disposition Score'].mean().reset_index()

    grouped = grouped.sort_values(by='Disposition Score', ascending=False)
    return grouped

def weighed_effects_persons():
    df = pd.read_csv("Soft Skillet_ October Data Live - Activity Data vOct.csv")
    
    # Use .loc to modify a slice of the DataFrame
    new_df = df[(df["Pitch"] == "AI") | (df["Pitch"] == "Operator") | (df["Pitch"] == "Smooth")].copy()
    # print(new_df)

    weights = {
        'Engaged': 2,
        'Deferred to Other Stakeholder': 1,
        'No Interest': 0,
        'No interest': 0
    }

    person_weight = {
        'Owner': 2,  
        'Manager': 1.0
    }

    # Set the 'Disposition Score' and 'Person Weight' with .loc to avoid SettingWithCopyWarning

    new_df.loc[:, 'Disposition Score'] = new_df['Disposition'].map(weights)
    new_df.loc[:, 'Person Weight'] = new_df['Person'].map(person_weight)


    # Calculate weighted disposition score
    new_df.loc[:, 'Weighted Disposition Score'] = new_df['Disposition Score'] * new_df['Person Weight']

    # Group by Pitch and calculate the mean weighted disposition score
    grouped = new_df.groupby('Pitch')['Weighted Disposition Score'].mean().reset_index()


    # Sort by weighted score
    grouped = grouped.sort_values(by='Weighted Disposition Score', ascending=False)
    return grouped


# Call the functions
weighted_normal = weighted_effects()
print(weighted_normal)

manager_owner_effects = weighed_effects_persons()
print(manager_owner_effects)
