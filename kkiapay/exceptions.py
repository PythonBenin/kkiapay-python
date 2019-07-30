class KkiapayException(Exception):
    pass


class KKiapayAlogrithmException(Exception):
    def __init__(self, algorithms):
        Exception.__init__(self,
                           "algorithm must be {}".format(
                               " or ".join(" if it's ".join(algorithm) for algorithm in algorithms.items())))


class KKiapayDestinationTypeException(Exception):
    def __init__(self, algorithms):
        Exception.__init__(self,
                           "destination_type must be {}".format(
                               " or ".join(" if it's ".join(algorithm) for algorithm in algorithms.items())))
