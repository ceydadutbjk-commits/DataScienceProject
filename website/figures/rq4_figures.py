import pandas as pd
import plotly.graph_objects as go


rq4_df = pd.read_csv("data/rq4_data.csv")


def create_rq4_figure(metric="index_gap"):
    """Create a dynamic range plot for Research Question 4."""

    metric_map = {
        "index_gap": {
            "start": "gap_start",
            "end": "gap_end",
            "title": "CPI–PPI Gap by Period",
            "xaxis": "CPI–PPI gap",
        },
        "butter_cpi": {
            "start": "butter_start",
            "end": "butter_end",
            "title": "Butter CPI by Period",
            "xaxis": "Butter CPI",
        },
        "dairy_ppi": {
            "start": "ppi_start",
            "end": "ppi_end",
            "title": "Dairy PPI by Period",
            "xaxis": "Dairy PPI",
        },
    }

    selected = metric_map[metric]

    start_values = rq4_df[selected["start"]]
    end_values = rq4_df[selected["end"]]
    periods = rq4_df["period"]

    line_x = []
    line_y = []

    for start, end, period in zip(start_values, end_values, periods):
        line_x.extend([start, end, None])
        line_y.extend([period, period, None])

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=line_x,
            y=line_y,
            mode="lines",
            line=dict(color="gray", width=3),
            showlegend=False,
        )
    )

    fig.add_trace(
        go.Scatter(
            x=start_values,
            y=periods,
            mode="markers",
            marker=dict(size=12),
            name="Start",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=end_values,
            y=periods,
            mode="markers",
            marker=dict(size=12),
            name="End",
        )
    )

    fig.update_layout(
        title=selected["title"],
        xaxis_title=selected["xaxis"],
        yaxis_title="Period",
        height=450,
    )

    return fig