"""
Module containing custom exception classes for Pyrus.

Classes:
    - PyrusException: Base class for all Pyrus exceptions.
    - InvalidConfigurationError: Raised when the Pyrus configuration is invalid.
    - InvalidArgumentError: Raised when an invalid argument is passed to a Pyrus function.
    - APIError: Raised when an error occurs while communicating with an API.
    - HTTPError: Raised when an HTTP error occurs while making an API request.
    - FileError: Raised when an error occurs while reading or writing a file.
"""

class PyrusException(Exception):
    """Base exception class for Pyrus.

    This class is intended to be subclassed by specific exceptions for Pyrus,
    to allow for more specific error handling.

    Args:
        message (str): The error message to display.

    Attributes:
        message (str): The error message associated with the exception.
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class UnsupportedFileTypeError(PyrusException):
    """Exception raised when trying to read or write an unsupported file type."""

    def __init__(self, file_path):
        super().__init__(f"The file type of '{file_path}' is not supported.")
        self.file_path = file_path
