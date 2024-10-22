import plotly.graph_objects as go
import pandas as pd
from data_analysis.call_metrics import no_answer_frequency, answer_frequency, owner_frequency, manager_frequency


def plot_call_connect_pie_chart():
    case_study = pd.read_csv("Soft Skillet_ October Data Live - Activity Data vOct.csv")
    counter_no_answer = no_answer_frequency(case_study)
    counter_answer = answer_frequency(case_study)
    
    labels = ["No Answer", "Connected"]
    values = [counter_no_answer, counter_answer]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                                 insidetextorientation='radial')])
    
    return fig
    # fig.show()


def plot_owner_manager_pickup_pie_chart():
    case_study = pd.read_csv("Soft Skillet_ October Data Live - Activity Data vOct.csv")
    counter_owner = owner_frequency(case_study)
    counter_manager = manager_frequency(case_study)
    
    labels = ["Owner Pickup", "Manger Pickup"]
    values = [counter_owner, counter_manager]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                                 insidetextorientation='radial')])
    
    return fig
    # fig.show()

# plot_call_connect_pie_chart(case_study)
# plot_owner_manager_pickup_pie_chart(case_study)
