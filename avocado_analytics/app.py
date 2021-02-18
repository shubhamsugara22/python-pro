import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
from dash.dependencies import Output, Input


# intial data queried for dashboard
data = pd.read_csv("avocado.csv")
data = data.query("type == 'conventional' and region == 'Albany'")
data['Date'] = pd.to_datetime(data['Date'], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)

app = dash.Dash(__name__)
external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    }
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Avocado analytics understand your avocados!"

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="🥑", className="header-emoji"),
                html.H1(children="avocado analytics",
                        className="header-title"),
                html.P(
                    children="Analyze the behavior of avocado prices  and number of avocados sold in the US between 2015  and 2018",
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Region", className="menu-title"),
                dcc.Dropdown(
                    id="region-filter",
                    options=[
                        {"label": region, "value": region}
                        for region in np.sort(data.region.unique())
                    ],
                    value="Albany",
                    clearable=False,
                    className="dropdown",
                )
            ]
        )

        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="price-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["Date"],
                                    "y":data["AveragePrice"],
                                    "type":"lines",
                                    "hovertemplate":"$%{y:.2f}"
                                                    "<extra></extra>",
                                },
                            ],
                            "layout":{
                                "title": {
                                    "text": "Average price of avocados",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {
                                    "tickprefix": "$",
                                    "fixedrange": True,
                                },
                                "colorway": ["#17B897"],
                            },
                        },
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="volume-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                                {
                                    "x": data["Date"],
                                    "y":data["Total Volume"],
                                    "type":"lines",
                                },
                            ],
                            "layout":
                            {
                                "title": {
                                    "text": "Avocado sold",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                                "colorway": ["#E12D39"],
                            },
                        },
                    ),
                    className="card",
                ),
            ],
            className="wrapper"
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
