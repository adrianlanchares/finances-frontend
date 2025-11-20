import streamlit as st

from src.utils.database import (
    get_transaction,
    get_transaction_list,
    get_balance,
    create_transaction,
)
from src.utils.plots import plot_total_money


def dashboard():
    st.title("Dashboard")

    # BALANCES #############################################################
    st.header("Balance")
    balances = get_balance()

    tarjeta_color = "FA3D2E"  # Example color for 'tarjeta'
    efectivo_color = "38C945"  # Example color for 'efectivo'
    ahorros_color = "48BBD1"  # Example color for 'ahorros'

    account_colors = {
        "tarjeta": tarjeta_color,
        "efectivo": efectivo_color,
        "ahorros": ahorros_color,
    }

    account_columns = st.columns(3)

    for account, column in zip(balances, account_columns):
        with column:
            balance = balances[account]
            color = account_colors[account]

            st.markdown(
                f"""
                <div style="background-color: #{color}; padding: 10px; border-radius: 5px; margin-bottom: 10px;">
                    <h3 style="color: white; margin: 0; text-align: center;">{balance:.2f}€</h3>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # PLOTS ################################################################
    st.header("Plots")
    st.subheader("Total Money Over Time")
    fig = plot_total_money()
    st.plotly_chart(fig, width="stretch")
