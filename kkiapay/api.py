from .base import KkiapayBase


class Kkiapay(KkiapayBase):
    def __init__(
        self, public_key: str, private_key: str, secret: str, sandbox=False
    ) -> None:
        r"""Initialize Kkiapay client.
        :param public_key: Public key from https://app.kkiapay.me/dashboard/developers/keys.
        :param private_key: Provate key from https://app.kkiapay.me/dashboard/developers/keys.
        :param secret: Kiapay secret from https://app.kkiapay.me/dashboard/developers/keys.
        :param sandbox: A boolean value to specify the environment (Sandbox or Live).
        """
        self._initialize_credentials(public_key, private_key, secret, sandbox)

    def verify_transaction(self, transaction_id: str) -> dict:
        r"""Verify a transaction.
        :param transaction_id: transaction ID
        """
        return self._verify_transaction(transaction_id)

    def refund_transaction(self, transaction_id: str) -> dict:
        r"""Refund a specific transaction.
        :param transaction_id: transaction ID
        """
        return self._refund_transaction(transaction_id)
