from __init__ import *

SUPPORTED_FILE_TYPES = {
    'datatable': ['csv', 'xls', 'xlsx', 'json'],
    'image': [],
    'audio': [],
    'text': [],
}


class File:

    def __init__(self, file, data=None, description=None):
        self.file = file
        self.data = data
        self.extension = file.rsplit(".", 1)[-1]
        self.description = description


class DataTable(File):

    def __init__(self):
        self.file_types = SUPPORTED_FILE_TYPES['datatable']

    def read(self):

        # If file is not supported
        if self.extension not in self.file_types:
            raise ValueError(f'File type .{self.extension} not supported.')

        # If file extension is excel format
        if self.extension == 'xlsx' or self.extension == 'xls':
            df = pd.read_excel(
                self.file, index_col=False)  # Extract as excel file

        # If file extension is csv
        elif self.extension == 'csv':
            df = pd.read_csv(
                self.file, index_col=False, engine='python', encoding='UTF-8')  # Extract as csv

        # If file extension is json
        elif self.extension == 'json':
            df = pd.read_json(self.file)

        return df

    def write(self):

        # get current date
        date_string = str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))

        # Create full output filename, using output_filename and date
        file = f'{self.file}_{self.description}_{date_string}.xlsx'

        # export the dataframe with full output name
        self.data.to_excel(file, encoding='Latin1')


class Image(File):
    pass


class Audio(File):
    pass
