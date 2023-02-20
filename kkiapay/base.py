from .utils import make_request

SANDBOX_BASE_URL = "https://api-sandbox.kkiapay.me"
PRODUCTION_BASE_URL = "https://api.kkiapay.me"


class KkiapayBase:
    def _initialize_credentials(self, public_key: str, private_key: str, secret: str, sandbox: bool) -> None:
        self.public_key             = public_key
        self.private_key            = private_key
        self.secret                 = secret
        self.is_sandbox_environment = sandbox

    def _build_request_headers(self) -> dict:
        return {
            "Accept": "application/json",
            "X-SECRET-KEY": self.secret,
            "X-API-KEY": self.public_key,
            "X-PRIVATE-KEY": self.private_key,
        }

    def _build_request_url(self, path: str) -> str:
        BASE_URL = SANDBOX_BASE_URL if self.is_sandbox_environment else PRODUCTION_BASE_URL
        return f"{BASE_URL}/{path}"

    def _verify_transaction(self, transaction_id: str):
        return make_request(
            "post",
            self._build_request_url("api/v1/transactions/status"),
            json={"transactionId": transaction_id},
            headers=self._build_request_headers()
        )

    def _refund_transaction(self, transaction_id: str):
        return make_request(
            "post",
            self._build_request_url("api/v1/transactions/revert"),
            json={"transactionId": transaction_id},
            headers=self._build_request_headers()
        )
