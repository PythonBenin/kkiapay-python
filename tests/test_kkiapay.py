from .context import kkiapay
from kkiapay import Kkiapay
import responses


@responses.activate
def test_verify_transaction():
    responses.add(
        responses.POST,
        "https://api-sandbox.kkiapay.me/api/v1/transactions/status",
        json={
            "performed_at": "2023-02-20T17:44:47.842Z",
            "received_at": 1676915100302,
            "type": "DEBIT",
            "status": "SUCCESS",
            "source": "MOBILE_MONEY",
        },
    )

    k = Kkiapay("public_key", "private_key", "secret", True)

    response = k.verify_transaction("123")
    assert response["type"] == "DEBIT"


@responses.activate
def test_refund_transaction():
    responses.add(
        responses.POST,
        "https://api-sandbox.kkiapay.me/api/v1/transactions/revert",
        json={"code": "SUCCESS", "description": "REVERTED", "transactionId": "123"},
    )

    k = Kkiapay("public_key", "private_key", "secret", True)

    response = k.refund_transaction("123")
    assert response == {
        "code": "SUCCESS",
        "description": "REVERTED",
        "transactionId": "123",
    }
