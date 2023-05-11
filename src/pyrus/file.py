from __init__ import *

SUPPORTED_FILE_TYPES = {
    'datatable': ['csv', 'xls', 'xlsx', 'json'],
    'image': [],
    'audio': [],
    'text': [],
}

class DataTable:

    """
    A class that reads or writes a data table file.

    Attributes:
        file_types (list): A list of supported file types for data tables.
        file (str): The path of the data table file.
        extension (str): The extension of the data table file.
    """

    def __init__(self, file):

        """
        Initializes a DataTable instance.

        Args:
            file (str): The path of the data table file.

        Raises:
            ValueError: If the file type is not supported.
        """
        
        self.file_types = SUPPORTED_FILE_TYPES['datatable']
        self.file = file
        self.extension = file.rsplit(".", 1)[-1]

        if self.extension not in self.file_types:
            raise ValueError(f'File type .{self.extension} not supported.')

    def read(self):

        """
        Reads a data table file and returns a pandas dataframe.

        Returns:
            pandas.DataFrame: A dataframe of the read file.
        """

        # If file is not supported
        if self.extension not in self.file_types:
            raise ValueError(f'File type .{self.extension} not supported.')

        # If file extension is excel format, read as excel format
        if self.extension == 'xlsx' or self.extension == 'xls':
            df = pd.read_excel(
                self.file, index_col=False)

        # If file extension is csv, read as csv
        elif self.extension == 'csv':
            df = pd.read_csv(self.file, index_col=False, engine='python', encoding='UTF-8')

        # If file extension is json, read as json
        elif self.extension == 'json':
            df = pd.read_json(self.file)

        return df

    def write(self):
        """
        Writes a dataframe to a file.

        The file name is constructed from the original file name and current timestamp.
        """

        # get current date
        date_string = str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))

        # Create full output filename, using output_filename and date
        file = f'{self.file}_{self.description}_{date_string}.xlsx'

        # export the dataframe with full output name
        self.data.to_excel(file, encoding='Latin1')

"""
class Image(File):
    pass


class Audio(File):
    pass
    
"""
