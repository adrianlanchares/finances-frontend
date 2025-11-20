import pandas as pd
import requests  # type: ignore
import os
import dotenv

from typing import Dict, Any, Optional

dotenv.load_dotenv()
BACKEND_URL = os.getenv("BACKEND_URL")
SSL_CERT_PATH = os.getenv("SSL_CERT_PATH")
if SSL_CERT_PATH is None:
    SSL_CERT_PATH = True  # type: ignore


def get_transaction(id: int) -> Dict[str, Any]:
    """
    Gets details of a single transaction

    Args:
        id (int): Transaction id
    Returns:
        Dict[str, Any]: Dictionary containing transaction information
    """
    response = requests.get(BACKEND_URL + f"/{id}", verify=SSL_CERT_PATH)  # type: ignore

    return response.json()


def get_transaction_list(query_params: Optional[Dict[str, Any]] = None) -> pd.DataFrame:
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
    url_params = ""
    if query_params is not None:
        url_params += "?"
        for filter in query_params:
            url_params += f"{filter}={query_params[filter]}&"

    response = requests.get(BACKEND_URL + url_params, verify=SSL_CERT_PATH)  # type: ignore

    return pd.DataFrame(response.json())


def create_transaction(transaction: Dict[str, Any]) -> bool:
    """
    Creates a transaction in the database

    Args:
        transaction (Dict[str, Any]): Transaction data
    Returns:
        bool: Whether the creation went OK or not.
    """
    response = requests.post(
        BACKEND_URL + "/create/",  # type: ignore
        transaction,
        verify=SSL_CERT_PATH,
    )

    return True if response.status_code == 201 else False


def get_balance() -> Dict[str, int]:
    """
    Get the current balance in each account

    Returns:
        Dict[str, int]: Dictonary containing account: balance
    """
    balances = {"tarjeta": 0, "efectivo": 0, "ahorros": 0}
    response = requests.get(BACKEND_URL + "/balance/", verify=SSL_CERT_PATH)  # type: ignore

    for account in response.json():
        balances[account] = response.json()[account]

    return balances
