import pandas as pd
from plotly.graph_objects import Figure

from src.utils.database import get_balance, get_transaction, get_transaction_list

from typing import Dict, Any


def plot_total_money(filters: Dict[str, Any]) -> Figure:
    """Plot the total money over time.

    Args:
        filters (Dict[str, Any]): Filters to apply to the plot
    Returns:
        Figure: Plotly figure object with the total money plot.
    """

    transactions = get_transaction_list(filters)

    transactions["signed_amount"] = transactions.apply(
        lambda row: row["amount"] if row["cashflow"] == "income" else -row["amount"],
        axis=1,
    )
    transactions["accumulated"] = transactions["signed_amount"].cumsum()

    # Make the same plot with Plotly
    fig = Figure()
    fig.add_trace(
        {
            "x": transactions["date"],
            "y": transactions["accumulated"],
            "mode": "lines+markers",
            "name": "Total Money",
            "marker": {"size": 1},
            "line": {"shape": "hv"},
        }
    )

    fig.update_layout(
        margin=dict(t=0),
    )

    return fig
