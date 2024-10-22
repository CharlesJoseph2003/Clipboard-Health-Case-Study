from dash import html
from dash import dcc
import pandas as pd
import dash_mantine_components as dmc
from plots.ai_graphs import plot_ai_seating_pie_chart, plot_ai_seating_owner_pie_chart, plot_ai_seating_manager_pie_chart
from plots.operator_graphs import plot_operator_pie_chart, plot_operator_owner_pie_chart, plot_operator_manager_pie_chart
from plots.smooth_revenue_graphs import plot_smooth_revenue_pie_chart, plot_smooth_revenue_owner_pie_chart, plot_smooth_revenue_manager_pie_chart
from plots.cross_analysis_graphs import plot_compare_pitches_bar_chart, plot_compare_pitches_owner_bar_chart,\
plot_compare_pitches_manager_bar_chart, plot_compare_engagement_pie_chart

def create_layout_ai():
    ai_layout = html.Div(children=[
        dmc.SimpleGrid(
            cols = 2,
            spacing= 'sm',
            children=[
                dcc.Graph(figure=plot_ai_seating_pie_chart()),
                dcc.Graph(figure=plot_ai_seating_owner_pie_chart()),
                dcc.Graph(figure=plot_ai_seating_manager_pie_chart())
            ]
        )

    ])
    return ai_layout

def create_layout_operator():
    operator_layout = html.Div(children=[
        dmc.SimpleGrid(
            cols = 2,
            spacing= 'sm',
            children=[
                dcc.Graph(figure=plot_operator_pie_chart()),
                dcc.Graph(figure=plot_operator_owner_pie_chart()),
                dcc.Graph(figure=plot_operator_manager_pie_chart())
            ]
        )

    ])
    return operator_layout

def create_layout_smooth():
    smooth_layout = html.Div(children=[
        dmc.SimpleGrid(
            cols = 2,
            spacing= 'sm',
            children=[
                dcc.Graph(figure=plot_smooth_revenue_pie_chart()),
                dcc.Graph(figure=plot_smooth_revenue_owner_pie_chart()),
                dcc.Graph(figure=plot_smooth_revenue_manager_pie_chart())
            ]
        )

    ])
    return smooth_layout

def create_layout_comparison():
    comparison_layout = html.Div(children=[
        dmc.SimpleGrid(
            cols = 2,
            spacing= 'sm',
            children=[
                dcc.Graph(figure=plot_compare_pitches_bar_chart()),
                dcc.Graph(figure=plot_compare_pitches_owner_bar_chart()),
                dcc.Graph(figure=plot_compare_pitches_manager_bar_chart()),
                dcc.Graph(figure=plot_compare_engagement_pie_chart())
            ]
        )

    ])
    return comparison_layout
