import dash
from layout.app_layout import create_layout
import dash_mantine_components as dmc

app = dash.Dash(__name__)
layout = create_layout()
app.layout = layout
if __name__ == '__main__':
    app.run_server(debug=True)