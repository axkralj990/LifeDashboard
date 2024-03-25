import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ..config.mapping import TransactionsMapping
from ..data.source import DataSource
from . import ids

def render(app: Dash, source: DataSource) -> html.Div:
    @app.callback(
        Output(ids.BAR_CHART_TIME_2, "children"),
        [
            Input(ids.YEAR_DROPDOWN, "value"),
            Input(ids.MONTH_DROPDOWN, "value"),
            Input(ids.CATEGORY_1_DROPDOWN, "value"),
            Input(ids.CATEGORY_2_DROPDOWN, "value")
        ],
    )
    def update_bar_chart(
        years: list[str],
        months: list[str],
        category_1: list[str],
        category_2: list[str]
    ) -> html.Div:
        filtered_source = source.filter(years, months, category_1, category_2)
        if not filtered_source.row_count:
            return html.Div("No data to display", id=ids.BAR_CHART_TIME_2)
                            
        fig = px.bar(
            filtered_source.create_pivot_table([TransactionsMapping.YEAR_MONTH['object'], TransactionsMapping.CATEGORY_2['object']]),
            x=TransactionsMapping.YEAR_MONTH['object'],
            y=TransactionsMapping.AMOUNT['object'],
            color=TransactionsMapping.CATEGORY_2['object'],
            labels={
                TransactionsMapping.CATEGORY_2['object']: TransactionsMapping.CATEGORY_2['label'],
                TransactionsMapping.AMOUNT['object']: TransactionsMapping.AMOUNT['label'],
                TransactionsMapping.YEAR_MONTH['object']: TransactionsMapping.YEAR_MONTH['label']
            },
        )
        
        fig.update_layout(showlegend=False)

        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART_TIME_2)

    return html.Div(id=ids.BAR_CHART_TIME_2)