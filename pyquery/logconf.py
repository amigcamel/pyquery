import logging


class Logger:

    def __init__(self, logger_name):

        formatter = logging.Formatter('[%(levelname)-5s] %(message)s')

        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)

        sh = logging.StreamHandler()
        sh.setLevel(logging.DEBUG)
        sh.setFormatter(formatter)

        logger.addHandler(sh)
        self._logger = logger

    def __getattr__(self, name):
        return getattr(self._logger, name)
