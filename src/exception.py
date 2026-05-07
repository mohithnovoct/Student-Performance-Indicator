import logging
import traceback


logger = logging.getLogger(__name__)

class AppException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.traceback = traceback.format_exc()
        logger.error(f"{message}\n{self.traceback}")