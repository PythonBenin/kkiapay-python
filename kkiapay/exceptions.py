from .utils import DESTINATION_TYPES, ALGORITHMS


class KkiapayException(Exception):
    message = None
    details = None

    def __str__(self):
        return self.message + " or ".join(" if it's ".join(self.details))


class KKiapayAlgorithmException(KkiapayException):
    details = ALGORITHMS.values()
    message = "algorithms must be "


class KKiapayDestinationTypeException(KkiapayException):
    details = DESTINATION_TYPES.values()
    message = "destination_type must be "
