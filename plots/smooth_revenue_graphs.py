import plotly.graph_objects as go
import pandas as pd
from data_analysis.smooth_revenue_analysis import smooth_metrics, smooth_metrics_owner, smooth_metrics_manager


def plot_smooth_revenue_pie_chart():
    case_study = pd.read_csv("Soft Skillet_ October Data Live - Activity Data vOct.csv")

    no_interest_count, engaged_count, deferred_count = smooth_metrics(case_study)

    labels = ["No Interest", "Engaged", "Deferred"]
    values = [no_interest_count, engaged_count, deferred_count]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                                 insidetextorientation='radial')])
    
    return fig
    # fig.show()

def plot_smooth_revenue_owner_pie_chart():
    case_study = pd.read_csv("Soft Skillet_ October Data Live - Activity Data vOct.csv")

    no_interest_count, engaged_count, deferred_count = smooth_metrics_owner(case_study)

    labels = ["Owner No Interest", "Owner Engaged", "Owner Deferred"]
    values = [no_interest_count, engaged_count, deferred_count]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                                 insidetextorientation='radial')])
    
    return fig
    # fig.show()


def plot_smooth_revenue_manager_pie_chart():
    case_study = pd.read_csv("Soft Skillet_ October Data Live - Activity Data vOct.csv")

    no_interest_count, engaged_count, deferred_count = smooth_metrics_manager(case_study)

    labels = ["Manager No Interest", "Manager Engaged", "Manager Deferred"]
    values = [no_interest_count, engaged_count, deferred_count]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                                 insidetextorientation='radial')])
    
    # return fig
    return fig

# smooth_revenue_graph = plot_smooth_revenue_pie_chart(case_study)
# smooth_revenue_owner_graph = plot_smooth_revenue_owner_pie_chart(case_study)
# smooth_revenue_manager_graph = plot_smooth_revenue_manager_pie_chart(case_study)

