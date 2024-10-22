import plotly.graph_objects as go
import pandas as pd
from ai_analysis import ai_seating_metrics, ai_seating_metrics_manager, ai_seating_metrics_owner
from operator_analysis import operator_metrics, operator_metrics_owner, operator_metrics_manager
from smooth_revenue_analysis import smooth_metrics, smooth_metrics_owner, smooth_metrics_manager

case_study = pd.read_csv("Soft Skillet_ October Data Live - Activity Data vOct.csv")

def plot_compare_engagement_pie_chart(df):
    _, engaged_count_ai,_ = ai_seating_metrics(df)
    _, engaged_count_operator,_ = operator_metrics(df)
    _, engaged_count_smooth,_ = smooth_metrics(df)

    labels = ["AI", "Operator", "Smooth"]
    values = [engaged_count_ai, engaged_count_operator, engaged_count_smooth]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                                 insidetextorientation='radial')])
    return fig
    # fig.show()


def plot_compare_pitches_pie_chart(df):
    no_interest_ai, engaged_count_ai, deferred_ai = ai_seating_metrics(df)
    no_interest_operator, engaged_count_operator, deferred_operator = operator_metrics(df)
    no_interest_smooth, engaged_count_smooth, deferred_smooth = smooth_metrics(df)

    labels = ['AI Seating', 'Operator', 'Smooth Revenue']
    fig = go.Figure(data=[
        go.Bar(name='Engaged', x=labels, y=[engaged_count_ai, engaged_count_operator, engaged_count_smooth]),
        go.Bar(name='Deferred to Other Stakeholder', x=labels, y=[deferred_ai, deferred_operator, deferred_smooth]),
        go.Bar(name='No Interest', x=labels, y=[no_interest_ai, no_interest_operator, no_interest_smooth])])
    fig.update_layout(barmode='stack')
    fig.show()

def plot_compare_pitches_owner_pie_chart(df):
    no_interest_ai, engaged_count_ai, deferred_ai = ai_seating_metrics_owner(df)
    no_interest_operator, engaged_count_operator, deferred_operator = operator_metrics_owner(df)
    no_interest_smooth, engaged_count_smooth, deferred_smooth = smooth_metrics_owner(df)

    labels = ['AI Seating', 'Operator', 'Smooth Revenue']
    fig = go.Figure(data=[
        go.Bar(name='Engaged', x=labels, y=[engaged_count_ai, engaged_count_operator, engaged_count_smooth]),
        go.Bar(name='Deferred to Other Stakeholder', x=labels, y=[deferred_ai, deferred_operator, deferred_smooth]),
        go.Bar(name='No Interest', x=labels, y=[no_interest_ai, no_interest_operator, no_interest_smooth])])
    fig.update_layout(barmode='stack')
    fig.show()

def plot_compare_pitches_manager_pie_chart(df):
    no_interest_ai, engaged_count_ai, deferred_ai = ai_seating_metrics_manager(df)
    no_interest_operator, engaged_count_operator, deferred_operator = operator_metrics_manager(df)
    no_interest_smooth, engaged_count_smooth, deferred_smooth = smooth_metrics_manager(df)

    labels = ['AI Seating', 'Operator', 'Smooth Revenue']
    fig = go.Figure(data=[
        go.Bar(name='Engaged', x=labels, y=[engaged_count_ai, engaged_count_operator, engaged_count_smooth]),
        go.Bar(name='Deferred to Other Stakeholder', x=labels, y=[deferred_ai, deferred_operator, deferred_smooth]),
        go.Bar(name='No Interest', x=labels, y=[no_interest_ai, no_interest_operator, no_interest_smooth])])
    fig.update_layout(barmode='stack')
    fig.show()


# engagement = plot_compare_engagement_pie_chart(case_study)
# compare_pitches = plot_compare_pitches_pie_chart(case_study)
# compare_pitches_owner = plot_compare_pitches_owner_pie_chart(case_study)
# compare_pitches_manager = plot_compare_pitches_manager_pie_chart(case_study)