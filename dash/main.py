# -*- coding: utf-8 -*-


import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_daq as daq
from dash.dependencies import Input, Output
from flask import request
import requests, math

external_stylesheets = [
    'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css',
    'https://codepen.io/chriddyp/pen/bWLwgP.css'
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),    
    html.Div(
             children=[
                html.H3(
                    [
                        "Sentiment Analyzer ",
                        html.Span(
                            id='company_name'
                        ),
                        " ?"
                    ],
                    className="h3 mb-3 font-weight-normal",
                    style={
                        'marginTop': '5px'
                    }
                ),
                html.Div(
                    [
                        dcc.Textarea(
                            className="form-control z-depth-1",
                            id="review",
                            rows="5",
                            placeholder="Write something here...",
                            style={'width': '50%', 'height': 200}
                        )
                    ],
                    className="form-group shadow-textarea"
                ),

                html.H5(
                    'Sentiment analysis'
                ),
                dbc.Progress(
                    children=html.Span(
                        id='length',
                        style={
                            'color': 'black',
                            'fontWeight': 'bold'
                        }
                    ),
                    id="progress",
                    striped=False,
                    animated=False,
                    style={
                        'marginBottom': '10px',
                        "height": "20px"
                    }
                ),
                # html.Div([     
                #     html.Label('Slider'),
                #     daq.Slider(
                #         min=1,
                #         max=5,
                #         marks={i: str(i) for i in range(1, 6)},
                #         value=5,
                #         size=150
                #     )
                # ],style={'marginBottom': '30px'}),
        
                # html.Button(
                #     [
                #         html.Span(
                #             "Submit",
                #             style={
                #                 "marginRight": "10px"
                #             }
                #         ),
                #         html.I(
                #             className="fa fa-paper-plane m-l-7"
                #         )
                #     ],
                #     className="btn btn-lg btn-primary btn-block",
                #     role="submit",
                #     id="submit_button",
                #     n_clicks_timestamp=0
                # ),
    
                html.Div(id='my-output')
                    
                ]),
                
],style={'width': '100%','padding-left':'20%', 'padding-right':'20%'},
)



@app.callback(
    [
    Output(component_id='my-output', component_property='children'),
    Output(component_id='length', component_property='children'),
    Output(component_id='progress', component_property='value'),
    Output(component_id='progress', component_property='color'),
    ],
    [Input(component_id='review', component_property='value')]
)
def update_output_div(review):
        
    response = requests.post(f"http://127.0.0.1:5000/engine", data={'review': review})
    value = response.json()
    return 'Output: {}'.format(value), f"{value}%", response.json(), 'success'


if __name__ == '__main__':
    app.run_server(debug=True, host='localhost', port=8050)

