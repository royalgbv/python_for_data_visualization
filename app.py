from dash import Dash, dcc, html
import pandas as pd
import plotly.express as px


app = Dash()

# load stock csv data
stocks= pd.read_csv('stock-prices.csv')

print(stocks.info())

# PROCESS THE DATA
# get the larges volume of stock
num= 5
largest= stocks.nlargest(num, 'Volume')
print(largest)

# make volume readable
largest['Volume']= round(stocks['Volume']/ 1_000_000,1)
print(largest)

# charts
pie_chart= px.pie(data_frame= largest,
                  values= 'Volume',
                  names= 'Company',
                  title= 'Top 5 Stock Companies by Volume')

bar_chart= px.bar(data_frame= largest,
                  x= 'Company',
                  y= 'Volume',
                  title= 'Company Volume in Bar Chart')

h_bar_chart= px.bar(data_frame= largest,
                  x= 'Company',
                  y= 'Volume',
                  orientation= 'h',
                  title= 'Compny Volume in Horizantal Bar Chart')

scatter_chart= px.scatter(data_frame= largest,
                  x= 'Company',
                  y= 'Volume',
                  orientation= 'h',
                  title= 'Company Volume in Scatter Chart')



app.layout= html.Div([
    html.H1('Visualizing Stock Prices'),
    dcc.Graph(figure= pie_chart),
    dcc.Graph(figure = bar_chart),
    html.Div([
        html.Div(dcc.Graph(figure=h_bar_chart), style={'flex': '1', 'padding': '10px'}),
        html.Div(dcc.Graph(figure=scatter_chart), style={'flex': '1', 'padding': '10px'}),
    ], style={'display': 'flex', 'flexDirection': 'row', 'justifyContent': 'space-between'}),
    
    html.P('By Royal G.'),
    ],
    style={
        'display':'flex',
        'flexDirection':'column',
        'backgroundColor': '#f9f9f9',
        'color': '#333333',
        'padding': '20px',
        'border': '1px solid #ccc',
        'borderRadius': 5,
        'textAlign': 'center',
        'marginTop': '15px'
    },)

app.run(debug=True)
