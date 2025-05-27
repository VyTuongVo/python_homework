from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata
import pandas as pd

#df = pldata.stocks(return_type='pandas', indexed=False, datetimes=True)
df = px.data.gapminder()
#print(df)
countries = pd.Series(df['country'].unique())

# Initialize Dash app
app = Dash(__name__)
#Adding from Task 5
server = app.server # <-- This is the line you need to add

# Layout
app.layout = html.Div([
    dcc.Dropdown(
        id="country-dropdown",
        options=[{"label": country, "value": country} for country in countries],
        value="Canada"
    ),
    dcc.Graph(id="gdp-growth")
])

# Callback for dynamic updates
@app.callback(
    Output("gdp-growth", "figure"),
    [Input("country-dropdown", "value")]
)
def update_graph(selected_country):
    new_df = df[df['country'] == selected_country]
    fig = px.line(new_df, x='year', y='gdpPercap',
                  title=f"GDP per Capita in {selected_country}")
    return fig

# Run the app
if __name__ == "__main__": 
    app.run(debug=True)