import dash_bootstrap_components as dbc
from dash import dcc, html
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, date

op_type_select = dbc.Select(
    id="op_type_select",
    options=[
        {"label": "Call", "value": "call"},
        {"label": "Put", "value": "put"},
    ],
    value="call",
)

op_ticker_input = dbc.Input(id="op_ticker_input", placeholder="AAPL", type="text")
op_strike_input = dbc.Input(id="op_strike_input", placeholder=200, type="number")
op_exp_input = dcc.DatePickerSingle(id="op_exp_input", date=datetime.now().date())
op_submit_btn = dbc.Button("Submit", id="submit", n_clicks=0, style={"width": "100px"})


def get_chart(ticker):
    ticker = yf.Ticker(ticker)
    close = ticker.history(period="1mo").reset_index()
    fig = go.Figure([go.Scatter(x=close["Date"], y=close["Close"])])
    return fig


input_groups = html.Div(
    [
        dbc.InputGroup(
            [dbc.InputGroupText("Ticker"), op_ticker_input],
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupText("Strike"),
                op_strike_input,
            ],
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupText("Expiration"),
                op_exp_input,
            ]
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupText("Type"),
                op_type_select,
            ],
        ),
    ],
    style={"width": "300px"},
)
