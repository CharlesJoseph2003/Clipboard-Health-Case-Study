import plotly.graph_objects as go
import pandas as pd
from operator_analysis import operator_metrics, operator_metrics_owner, operator_metrics_manager

case_study = pd.read_csv("Soft Skillet_ October Data Live - Activity Data vOct.csv")


def plot_operator_pie_chart(df):
    no_interest_count, engaged_count, deferred_count = operator_metrics(df)

    labels = ["No Interest", "Engaged", "Deferred"]
    values = [no_interest_count, engaged_count, deferred_count]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                                 insidetextorientation='radial')])
    
    return fig
    # fig.show()


def plot_operator_owner_pie_chart(df):
    no_interest_count, engaged_count, deferred_count = operator_metrics_owner(df)

    labels = ["Owner No Interest", "Owner Engaged", "Owner Deferred"]
    values = [no_interest_count, engaged_count, deferred_count]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                                 insidetextorientation='radial')])
    
    return fig
    # fig.show()


def plot_operator_manager_pie_chart(df):
    no_interest_count, engaged_count, deferred_count = operator_metrics_manager(df)

    labels = ["Manager No Interest", "Manager Engaged", "Manager Deferred"]
    values = [no_interest_count, engaged_count, deferred_count]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                                 insidetextorientation='radial')])
    
    return fig
    # fig.show()

operator_graph = plot_operator_pie_chart(case_study)
operator_owner_graph = plot_operator_owner_pie_chart(case_study)
operator_manager_graph = plot_operator_manager_pie_chart(case_study)