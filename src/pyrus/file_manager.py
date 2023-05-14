from . import pyrus_exceptions as pe
from . import *

class FileManager:
    
    """
    A utility class for reading and writing various types of files.

    Args:
        filename (str): The path to the file.

    Attributes:
        filepath (str): The path to the file.
        extension (str): The file extension.

    Methods:
        read(): Reads the file and returns its contents.
        write(data_to_write_to_file, add_date_to_filename=False): Writes the given data to the file.
        add_date(): Appends the current date and time to the file name.
        read_data_table(): Reads a table from a CSV, JSON, or Excel file and returns it as a pandas DataFrame.
        write_data_table(data_to_write_to_file): Writes a pandas DataFrame to a CSV, JSON, or Excel file.
        read_img(): Reads an image file and returns it as a PIL Image object.
        write_img(data_to_write_to_file): Writes a PIL Image object to an image file.
        read_video(): Reads a video file and returns it as a moviepy.VideoFileClip object.
        write_video(data_to_write_to_file): Writes a moviepy.VideoFileClip object to a video file.
        read_audio(): Reads an audio file and returns it as a pydub.AudioSegment object.
        write_audio(data_to_write_to_file): Writes a pydub.AudioSegment object to an audio file.
        read_text(): Reads a Microsoft Word document and returns it as a python-docx Document object.
        write_text(data_to_write_to_file): Writes a python-docx Document object to a Microsoft Word document.

    Raises:
        UnsupportedFileTypeError: If the file type is not supported.

    Examples:
        To read data from a CSV file:

        >>> fm = FileManager('data.csv')
        >>> data = fm.read()

        To write data to an Excel file with the current date appended to the file name:

        >>> fm = FileManager('data.xlsx')
        >>> fm.write(data_to_write_to_file, add_date_to_filename=True)

    """

    SUPPORTED_EXTENSIONS = {
        'data_table': {'.csv', '.json', '.xlsx', '.xls'},
        'image': {'.png', '.jpg', '.bmp', '.gif', '.tiff', '.webp', '.ppm'},
        'video': {'.mp4', '.avi', '.wmv', '.flv', '.mkv', '.ogv', '.mpeg', '.mov'},
        'audio': {'.mp3', '.wav', '.aac', '.flac', '.aiff', '.ogg'},
        'text': {'.doc', '.docx'}
    }


    def __init__(self, filepath):
        """
        Initialize a FileManager instance with the given filename.

        Parameters:
        -----------
        filepath: str
            The filepath, including name and extension, of the file to be read or written.
        """        
        self.filepath = filepath
        self.path_prefix, self.file_ext = os.path.splitext(filepath)
        self.filetype = self.get_filetype()

        if self.filetype is None:
            raise pe.UnsupportedFileTypeError(f"The file type of '{self.filepath}' is not supported. File types must be one of {self.SUPPORTED_EXTENSIONS[self.filetype]}.")
        
    def get_filetype(self):
        
        return next((filetype for filetype, ext in self.SUPPORTED_EXTENSIONS.items() if self.file_ext in ext), None)

    def read(self):
        """
        Read the file and return the contents.

        Returns:
        --------
        file: object
            The contents of the file.
        """        
        if self.filetype == 'data_table':
            self.read_data_table()
        
        elif self.filetype == 'image':
            file = self.read_img()

        elif self.filetype == 'video':
            file = self.read_video()

        elif self.filetype == 'audio':
            file = self.read_audio()

        elif self.filetype == 'text':
            file = self.read_text()

        else:
            raise pe.UnsupportedFileTypeError(f"The file type of '{self.filepath}' is not supported.")
        
        return file
        
    def write(self, data_to_write_to_file, add_date_to_filename=False):

        """
        Writes the given data to the file.

        Parameters:
        -----------
        data_to_write_to_file: object
            - The data to write to the file. For file types that require a specific object type, the
                following are expected:

            - Data Table:
                - CSV: pandas DataFrame
                - JSON: pandas DataFrame
                - Excel: pandas DataFrame

            - Image:
                - PNG: PIL.Image.Image
                - JPG: PIL.Image.Image
                - Bitmap: PIL.Image.Image
                - GIF: PIL.Image.Image
                - TIFF: PIL.Image.Image
                - WebP: PIL.Image.Image
                - PPM: PIL.Image.Image

            - Video: 
                - mp4: str, pathlib.Path, or bytes
                - avi: str, pathlib.Path, or bytes
                - wmv: str, pathlib.Path, or bytes
                - flv: str, pathlib.Path, or bytes
                - mkv: str, pathlib.Path, or bytes
                - ogv: str, pathlib.Path, or bytes
                - mpeg: str, pathlib.Path, or bytes
                - mov: str, pathlib.Path, or bytes

            - Audio:
                - mp3: str, pathlib.Path, or bytes
                - wav: str, pathlib.Path, or bytes
                - aac: str, pathlib.Path, or bytes
                - flac: str, pathlib.Path, or bytes
                - aiff: str, pathlib.Path, or bytes
                - ogg: str, pathlib.Path, or bytes

            - Text Processor:
                - doc: str, pathlib.Path, or bytes
                - docx: str, pathlib.Path, or bytes

                - CSV: pandas DataFrame
                - JSON: dict or list of dicts
                - Excel: pandas DataFrame
                - TXT: str

            - add_date_to_filename: bool, optional
                Whether to add the current date and time to the filename, default is False.
        """

        if add_date_to_filename:
            self.add_date()

        if self.filetype == 'data_table':
            self.write_data_table(data_to_write_to_file)
        
        elif self.filetype == 'image':
            self.write_img(data_to_write_to_file)

        elif self.filetype == 'video':
            self.write_video(data_to_write_to_file)

        elif self.filetype == 'audio':
            self.write_audio(data_to_write_to_file)

        elif self.filetype == 'text':
            self.write_text(data_to_write_to_file)

        else:
            raise pe.UnsupportedFileTypeError(f"The file type of '{self.filepath}' is not supported.")
        
    def add_date(self):
        """
        Adds the current date and time to the filename 
        of the file being managed by FileManager object.
        """        
        date_string = str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))

        self.filepath = f'{self.path_prefix}_{date_string}.{self.file_ext}'
    
    def read_data_table(self):
        """
        Reads a file and returns a pandas DataFrame object.
        
        Returns:
        file (pandas.DataFrame): DataFrame object created by reading the file.
        
        Raises:
        UnsupportedFileTypeError: If the file type is not supported.
        FileNotFoundError: If the file cannot be found in the specified filepath.
        """

        try:
            if self.file_ext == 'csv':
                file = pd.read_csv(self.filepath)
            
            elif self.file_ext == 'json':
                file = pd.read_json(self.filepath)

            elif self.file_ext == 'xlsx' or self.file_ext == 'xls':
                file = pd.read_excel(self.filepath)

        
        except FileNotFoundError:
            raise FileNotFoundError(f"Could not find file in specified path {self.filepath}. Please check sepcified path.")
        
        except PermissionError:
            raise PermissionError(f"It appears you do not have permission to read {self.filepath}. Please check path, or contact PC administrator.")
        
        return file

    def write_data_table(self, data_to_write_to_file):
        """
        Writes the data provided to a file with a filename specified by FileManager object.
        
        Args:
        data_to_write_to_file (pandas.DataFrame): DataFrame object containing the data to write.
        
        Raises:
        UnsupportedFileTypeError: If the file type is not supported.
        """
        try:        
            if self.file_ext == 'csv':
                data_to_write_to_file.to_csv(self.filepath)
            
            elif self.file_ext == 'json':
                data_to_write_to_file.to_json(self.filepath)

            elif self.file_ext == 'xlsx' or self.file_ext == 'xls':
                data_to_write_to_file.to_excel(self.filepath)
        
        except FileExistsError:
            raise FileExistsError(f"File with the path {self.file_ext} already exists. Please check filepath.")
        
        except PermissionError:
            raise PermissionError(f"It appears you do not have permission to write {self.filepath}. Please check path, or contact PC administrator.")

    def read_img(self):
        """
        Reads an image file and returns an Image object.
        
        Returns:
        file (PIL.Image.Image): Image object created by reading the file.
        
        Raises:
        UnsupportedFileTypeError: If the file type is not supported.
        FileNotFoundError: If the file cannot be found in the specified filepath.
        """
        try:   
            file = Image.open(self.filepath)
        
        except FileNotFoundError:
            raise FileNotFoundError(f"Could not find file in specified path {self.filepath}. Please check sepcified path.")
        
        except PermissionError:
            raise PermissionError(f"It appears you do not have permission to read {self.filepath}. Please check path, or contact PC administrator.")

        return file
    
    def write_img(self, data_to_write_to_file):
        """
        Writes the image data provided to a file with a filename specified by FileManager object.
        
        Args:
        data_to_write_to_file (PIL.Image.Image): Image object containing the data to write.
        
        Raises:
        UnsupportedFileTypeError: If the file type is not supported.
        """   
        try:     
            data_to_write_to_file.save(self.filepath)
        
        except FileExistsError:
            raise FileExistsError(f"File with the path {self.file_ext} already exists. Please check filepath.")       
        
        except PermissionError:
            raise PermissionError(f"It appears you do not have permission to write {self.filepath}. Please check path, or contact PC administrator.")         

    def read_video(self):
        """
        Reads a video file and returns a VideoFileClip object.
        
        Returns:
        file (moviepy.video.VideoFileClip.VideoFileClip): VideoFileClip object created by reading the file.
        
        Raises:
        UnsupportedFileTypeError: If the file type is not supported.
        FileNotFoundError: If the file cannot be found in the specified filepath.
        """
        try:        
            file = VideoFileClip(self.filepath)
        
        except FileNotFoundError:
            raise FileNotFoundError(f"Could not find file in specified path {self.filepath}. Please check sepcified path.")

        except PermissionError:
            raise PermissionError(f"It appears you do not have permission to read {self.filepath}. Please check path, or contact PC administrator.")       
        
        return file
    def write_video(self, data_to_write_to_file):
        """
        Writes the video data provided to a file with a filename specified by FileManager object.
        
        Args:
        data_to_write_to_file (moviepy.video.VideoFileClip.VideoFileClip): VideoFileClip object containing the data to write.
        
        Raises:
        UnsupportedFileTypeError: If the file type is not supported.
        """
        try:        
            data_to_write_to_file.write_videofile(self.filepath)
        
        except FileExistsError:
            raise FileExistsError(f"File with the path {self.file_ext} already exists. Please check filepath.")
        
        except PermissionError:
            raise PermissionError(f"It appears you do not have permission to write {self.filepath}. Please check path, or contact PC administrator.")

    def read_audio(self):
        """
        Reads an audio file and returns an AudioSegment object.
        
        Returns:
        file (pydub.AudioSegment.AudioSegment): AudioSegment object created by reading the file.
        
        Raises:
        UnsupportedFileTypeError: If the file type is not supported.
        FileNotFoundError: If the file cannot be found in the specified filepath.
        """    
        try:    
            file = AudioSegment.from_file(self.filepath, format=self.file_ext)
        
        except FileNotFoundError:
            raise FileNotFoundError(f"Could not find file in specified path {self.filepath}. Please check sepcified path.")        

        except PermissionError:
            raise PermissionError(f"It appears you do not have permission to read {self.filepath}. Please check path, or contact PC administrator.")
        
        return file
    
    def write_audio(self, data_to_write_to_file):
        """
        Writes the audio data provided to a file with a filename specified by FileManager object.
        
        Args:
        data_to_write_to_file (pydub.AudioSegment.AudioSegment): AudioSegment object containing the data to write.
        
        Raises:
        UnsupportedFileTypeError: If the file type is not supported.
        """
        try:        
            data_to_write_to_file.export(self.filepath, format=self.file_ext)
        
        except FileExistsError:
            raise FileExistsError(f"File with the path {self.file_ext} already exists. Please check filepath.")

        except PermissionError:
            raise PermissionError(f"It appears you do not have permission to write {self.filepath}. Please check path, or contact PC administrator.")

    def read_text(self):
        """
        Reads a text file and returns a docx.Document object.
        
        Returns:
        file (docx.document.Document): Document object created by reading the file.
        
        Raises:
        UnsupportedFileTypeError: If the file type is not supported.
        FileNotFoundError: If the file cannot be found in the specified filepath.
        """  
        try:      
            file = docx.Document(self.filepath)
        
        except FileNotFoundError:
            raise FileNotFoundError(f"Could not find file in specified path {self.filepath}. Please check sepcified path.")        

        except PermissionError:
            raise PermissionError(f"It appears you do not have permission to read {self.filepath}. Please check path, or contact PC administrator.")
        
        return file
    
    def write_text(self, data_to_write_to_file):
        """
        Writes a docx Document object to a Word document file.
        """
        try:        
            data_to_write_to_file.save(self.filepath)
        
        except FileExistsError:
            raise FileExistsError(f"File with the path {self.file_ext} already exists. Please check filepath.")
        
        except PermissionError:
            raise PermissionError(f"It appears you do not have permission to write {self.filepath}. Please check path, or contact PC administrator.")