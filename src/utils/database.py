import pandas as pd
import requests

from typing import Dict, Any

BACKEND_URL = "http://finances-backend:8008/transactions"


def get_transaction(id: int) -> Dict[str, Any]:
    """
    Gets details of a single transaction

    Args:
        id (int): Transaction id
    Returns:
        Dict[str, Any]: Dictionary containing transaction information
    """
    response = requests.get(BACKEND_URL + f"/{id}")

    return response.json()


def get_transaction_list(query_params: Dict[str, Any] = {}) -> pd.DataFrame:
    """
    Gets all of the transactions' data

    Arguments:
        query_params: Dictionary containing filters. Possible filters are:
            - minAmount
            - maxAmount
            - description
            - category
            - account
            - date
            - beforeDatetime
            - afterDatetime
            - skip
            - limit

    Returns:
        List[Dict[str, Any]]: List of transactions
    """
    url_params = "?"
    for filter in query_params:
        url_params += f"{filter}={query_params[filter]}&"

    response = requests.get(BACKEND_URL + url_params)

    return pd.DataFrame(response.json())


def create_transaction(transaction: Dict[str, Any]) -> bool:
    """
    Creates a transaction in the database

    Args:
        transaction (Dict[str, Any]): Transaction data
    Returns:
        bool: Whether the creation went OK or not.
    """
    response = requests.post(BACKEND_URL + "/create/", transaction)

    return True if response.status_code == 201 else False


def get_balance() -> Dict[str, int]:
    """
    Get the current balance in each account

    Returns:
        Dict[str, int]: Dictonary containing account: balance
    """
    response = requests.get(BACKEND_URL + "/balance/")

    return response.json()
