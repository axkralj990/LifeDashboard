from dash import Dash, html
from src.components import (
    bar_chart_cat_1,
    bar_chart_cat_2,
    bar_chart_time_1,
    bar_chart_time_2,
    cat_1_dropdown,
    cat_2_dropdown,
    month_dropdown,
    year_dropdown,
)

from ..data.source import DataSource

def create_layout(app: Dash, source: DataSource) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[
                    year_dropdown.render(app, source),
                    month_dropdown.render(app, source),
                    cat_1_dropdown.render(app, source),
                    cat_2_dropdown.render(app, source),
                ],
            ),
            bar_chart_cat_1.render(app, source),
            bar_chart_cat_2.render(app, source),
            bar_chart_time_1.render(app, source),
            bar_chart_time_2.render(app, source),
        ],
    )