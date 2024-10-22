import plotly.graph_objects as go
import pandas as pd
from ai_analysis import ai_seating_metrics, ai_seating_metrics_manager, ai_seating_metrics_owner

case_study = pd.read_csv("Soft Skillet_ October Data Live - Activity Data vOct.csv")

def plot_ai_seating_pie_chart(df):
    no_interest_count, engaged_count, deferred_count = ai_seating_metrics(df)

    labels = ["No Interest", "Engaged", "Deferred"]
    values = [no_interest_count, engaged_count, deferred_count]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                                 insidetextorientation='radial')])
    

    fig.show()

def plot_ai_seating_owner_pie_chart(df):
    no_interest_count, engaged_count, deferred_count = ai_seating_metrics_owner(df)

    labels = ["Owner No Interest", "Owner Engaged", "Owner Deferred"]
    values = [no_interest_count, engaged_count, deferred_count]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                                 insidetextorientation='radial')])
    
    return fig
    # fig.show()

def plot_ai_seating_manager_pie_chart(df):
    no_interest_count, engaged_count, deferred_count = ai_seating_metrics_manager(df)

    labels = ["Manager No Interest", "Manager Engaged", "Manager Deferred"]
    values = [no_interest_count, engaged_count, deferred_count]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                                 insidetextorientation='radial')])
    
    return fig
    # fig.show()



# ai_seating_graph = plot_ai_seating_pie_chart(case_study)
# ai_seating_owner_graph = plot_ai_seating_owner_pie_chart(case_study)
# ai_seating_manager_graph = plot_ai_seating_manager_pie_chart(case_study)