import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd


# intial data queried for dashboard
data = pd.read_csv("avocado.csv")
data = data.query("type == 'conventional' and region == 'Albany'")
data['Date'] = pd.to_datetime(data['Date'], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="avocado analytics"),
        html.P(
            children="Analyze the behavior of avocado prices  and number of avocados sold in the US between 2015  and 2018"
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y":data["AveragePrice"],
                        "type":"lines",
                    },
                ],
                "layout":{"title": "Average price of avocados"}
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y":data["Total Volume"],
                        "type":"lines",
                    },
                ],
                "layout":{"title": "Avocado sold"}
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
