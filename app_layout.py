from dash import html
import dash_mantine_components as dmc
from page_layouts import create_layout_ai, create_layout_operator, create_layout_smooth, create_layout_comparison

def create_layout():
    app_layout = html.Div(children=[
        html.H1(children="Clipboard Health Case Study", style={'textAlign': 'center'}),  # Corrected style property from 'text_align' to 'textAlign'

        dmc.Tabs(
            [
                dmc.TabsList(
                    [
                        dmc.Tab('Comparison', value='comparison'),
                        dmc.Tab('AI Seating', value='ai_seating'),  # Corrected value to match the TabsPanel value
                        dmc.Tab('Operator', value='operator'),
                        dmc.Tab('Smooth Revenue', value='smooth'),

                    ],
                    position='center',
                    grow=True
                ),
                dmc.TabsPanel(create_layout_comparison(), value='comparison'),
                dmc.TabsPanel(create_layout_ai(), value='ai_seating'),
                dmc.TabsPanel(create_layout_operator(), value='operator'),
                dmc.TabsPanel(create_layout_smooth(), value='smooth'),
            ],
            color='blue',
            orientation='horizontal',
            value='comparison'
        )
    ])
    return app_layout
