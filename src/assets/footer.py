from dash import html
import dash_bootstrap_components as dbc

import toml

with open("pyproject.toml", "r", encoding="UTF-8") as f:
    config = toml.load(f)
    
    version_num = config["tool"]["poetry"]["version"]

_footer = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col([html.Hr([], className = "hr-footer")], width = 12)
        ]),
        dbc.Row([
	        dbc.Col([], width = 1),
            dbc.Col([f"Dashboard Version Number: {version_num}"], width = 3),
            dbc.Col([], width =6),
	        dbc.Col([
                html.Ul([
                    html.Li([
                        html.A([ html.I(className="fa-brands fa-github me-3 fa-1x")], href="https://github.com/gabri-al"),
                        html.A([ html.I(className="fa fa-bitbucket-square me-3 fa-1x")], href="https://github.com/gabri-al")
                    ])
                ], className="list-unstyled d-flex justify-content-center justify-content-md-start")
            ], width = 2)
        ])
    ], fluid=True)
], className = "footer")