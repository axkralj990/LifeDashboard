from re import I
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from ..data.source import DataSource
from . import ids
from .dropdown_helper import to_dropdown_options
from ..config.mapping import ComponentsMapping, TransactionsMapping

def render(app: Dash, source: DataSource) -> html.Div:
    @app.callback(
        Output(ids.MONTH_DROPDOWN, "value"),
        [Input(ids.SELECT_ALL_MONTHS_BUTTON, "n_clicks"),
         Input(ids.YEAR_DROPDOWN, "value")],
    )
    def select_all_months(_: int, years: list[str]) -> list[str]:
        filtered_source = source.filter(years, None, None, None)
        return filtered_source.unique_months

    return html.Div(
        children=[
            html.H6(TransactionsMapping.MONTH['label']),
            dcc.Dropdown(
                id=ids.MONTH_DROPDOWN,
                options=to_dropdown_options(source.unique_months),
                value=source.unique_months,
                multi=True,
            ),
            html.Button(
                className="dropdown-button",
                children=[ComponentsMapping.SELECT_ALL],
                id=ids.SELECT_ALL_MONTHS_BUTTON,
                n_clicks=0,
            ),
        ]
    )