import plotly.graph_objects as go
import pandas as pd
from data_analysis.operator_analysis import operator_metrics, operator_metrics_owner, operator_metrics_manager

case_study = pd.read_csv("Soft Skillet_ October Data Live - Activity Data vOct.csv")


def plot_operator_pie_chart():
    case_study = pd.read_csv("Soft Skillet_ October Data Live - Activity Data vOct.csv")

    no_interest_count, engaged_count, deferred_count = operator_metrics(case_study)

    labels = ["No Interest", "Engaged", "Deferred"]
    values = [no_interest_count, engaged_count, deferred_count]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                                 insidetextorientation='radial')])
    fig.update_layout(
    title={
        'text': "Operator Overall Disposition Distribution",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    }
)
    
    return fig

def plot_operator_owner_pie_chart():
    case_study = pd.read_csv("Soft Skillet_ October Data Live - Activity Data vOct.csv")

    no_interest_count, engaged_count, deferred_count = operator_metrics_owner(case_study)

    labels = ["Owner No Interest", "Owner Engaged", "Owner Deferred"]
    values = [no_interest_count, engaged_count, deferred_count]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                                 insidetextorientation='radial')])
    fig.update_layout(
    title={
        'text': "Operator Disposition Distribution - Owner",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    }
)
    
    return fig


def plot_operator_manager_pie_chart():
    case_study = pd.read_csv("Soft Skillet_ October Data Live - Activity Data vOct.csv")

    no_interest_count, engaged_count, deferred_count = operator_metrics_manager(case_study)

    labels = ["Manager No Interest", "Manager Engaged", "Manager Deferred"]
    values = [no_interest_count, engaged_count, deferred_count]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                                 insidetextorientation='radial')])
    fig.update_layout(
    title={
        'text': "Operator Disposition Distribution -  Manager",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    }
)
    
    return fig
