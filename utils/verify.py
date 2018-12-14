from utils.logs import log


class Verify(object):
    @staticmethod
    def equals(expected, actual, message_on_fail):
        try:
            assert expected == actual, message_on_fail
        except AssertionError as err:
            err_type = err.__class__.__name__
            log.error(err_type)
            log.debug("\n\texpected: %s  \n\tactual:   %s", expected, actual)
            raise err

    @staticmethod
    def not_equals(expected, actual, message_on_fail):
        try:
            assert expected is not actual, message_on_fail
        except AssertionError as err:
            err_type = err.__class__.__name__
            log.error(err_type)
            log.debug("%s should not be equal to %s", expected, actual)
            raise err

    @staticmethod
    def true(condition, message_on_fail):
        try:
            assert condition, message_on_fail
        except AssertionError as err:
            err_type = err.__class__.__name__
            log.error(err_type)
            raise err

    @staticmethod
    def false(condition, message_on_fail):
        try:
            assert not condition, message_on_fail
        except AssertionError as err:
            err_type = err.__class__.__name__
            log.error(err_type)
            raise err

    @staticmethod
    def each(expected, actual, message_on_fail):
        """
        Compare two lists.
        Order of the lists can be different.
        Raise AssertionError if at least one mismatch was found between two lists.
        :param expected: list with expected values
        :param actual: list with actual values
        """
        result = set(actual) & set(expected)
        if len(expected) != len(result):
            raise AssertionError(message_on_fail)

    @staticmethod
    def contains(expected, actual, message_on_fail):
        try:
            assert expected in actual, message_on_fail
        except AssertionError as err:
            err_type = err.__class__.__name__
            log.debug("\n\texpected: %s value contains actual:   %s", expected, actual)
            log.error(err_type)
            raise err
