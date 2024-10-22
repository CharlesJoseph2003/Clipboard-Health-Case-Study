import plotly.graph_objects as go
import pandas as pd
from data_analysis.ai_analysis import ai_seating_metrics, ai_seating_metrics_manager, ai_seating_metrics_owner


def plot_ai_seating_pie_chart():
    case_study = pd.read_csv("Soft Skillet_ October Data Live - Activity Data vOct.csv")
    no_interest_count, engaged_count, deferred_count = ai_seating_metrics(case_study)

    labels = ["No Interest", "Engaged", "Deferred"]
    values = [no_interest_count, engaged_count, deferred_count]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                                 insidetextorientation='radial')])
    fig.update_layout(
        title={
            'text': "AI Seating Overall Disposition Distribution",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        }
    )
    
    return fig


def plot_ai_seating_owner_pie_chart():
    case_study = pd.read_csv("Soft Skillet_ October Data Live - Activity Data vOct.csv")

    no_interest_count, engaged_count, deferred_count = ai_seating_metrics_owner(case_study)

    labels = ["Owner No Interest", "Owner Engaged", "Owner Deferred"]
    values = [no_interest_count, engaged_count, deferred_count]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                                 insidetextorientation='radial')])
    fig.update_layout(
    title={
        'text': "AI Seating Disposition Distribution - Owner",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    }
)

    
    return fig


def plot_ai_seating_manager_pie_chart():
    case_study = pd.read_csv("Soft Skillet_ October Data Live - Activity Data vOct.csv")
    no_interest_count, engaged_count, deferred_count = ai_seating_metrics_manager(case_study)

    labels = ["Manager No Interest", "Manager Engaged", "Manager Deferred"]
    values = [no_interest_count, engaged_count, deferred_count]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                                 insidetextorientation='radial')])
    fig.update_layout(
    title={
        'text': "AI Seating Disposition Distribution - Manager",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    }
)
    

    
    return fig
