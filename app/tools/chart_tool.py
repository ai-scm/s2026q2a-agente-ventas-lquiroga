import plotly.express as px

def create_chart(df):

    x_col = df.columns[0]
    y_col = df.columns[1]

    fig = px.bar(
        df,
        x=x_col,
        y=y_col
    )

    return fig
