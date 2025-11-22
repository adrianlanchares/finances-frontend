import pandas as pd
from plotly.graph_objects import Figure

from src.utils.database import get_balance, get_transaction, get_transaction_list

from typing import Dict, Any, Optional


def plot_total_money(filters: Optional[Dict[str, Any]] = None) -> Figure:
    """Plot accumulated total money over time.

    Args:
        filters (Dict[str, Any]): Filters to apply to the plot
    Returns:
        Figure: Plotly figure object with the total money plot.
    """

    transactions: pd.DataFrame = get_transaction_list(filters)

    transactions["amount"] = transactions["amount"].astype(float)
    transactions["accumulated"] = transactions["amount"].cumsum()

    # Make the same plot with Plotly
    fig = Figure()
    fig.add_trace(
        {
            "x": transactions["datetime"],
            "y": transactions["accumulated"],
            "mode": "lines+markers",
            "name": "Total Money",
            "marker": {"size": 1},
            "line": {"shape": "hv"},
        }
    )

    return fig
