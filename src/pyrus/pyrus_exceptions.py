
class UnsupportedFileTypeError(Exception):
    """Exception raised when trying to read or write an unsupported file type."""

    def __init__(self, file_path):
        super().__init__(f"The file type of '{file_path}' is not supported.")
        self.file_path = file_path