import plotly.graph_objects as go
import pandas as pd
from call_metrics import no_answer_frequency, answer_frequency, owner_frequency, manager_frequency

case_study = pd.read_csv("Soft Skillet_ October Data Live - Activity Data vOct.csv")

counter_owner = owner_frequency(case_study)
counter_manager = manager_frequency(case_study)

def plot_call_connect_pie_chart(df):
    counter_no_answer = no_answer_frequency(df)
    counter_answer = answer_frequency(df)
    
    labels = ["No Answer", "Connected"]
    values = [counter_no_answer, counter_answer]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                                 insidetextorientation='radial')])
    

    fig.show()


def plot_owner_manager_pickup_pie_chart(df):
    counter_owner = owner_frequency(df)
    counter_manager = manager_frequency(df)
    
    labels = ["Owner Pickup", "Manger Pickup"]
    values = [counter_owner, counter_manager]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                                 insidetextorientation='radial')])
    

    fig.show()

plot_call_connect_pie_chart(case_study)
plot_owner_manager_pickup_pie_chart(case_study)
