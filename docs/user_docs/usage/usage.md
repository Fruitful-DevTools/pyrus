## pyrus.backoff

## pyrus.cache

## pyrus.file_manager

`file_manager` is a utility module that enables you to read and write different types of files. It provides you with the flexibility to read and write data tables, images, videos, audios, and text files in the formats supported by the module.

### Usage

To use the module, you can import the `FileManager` class as shown below:

```python
from file_manager import FileManager
```

You can then create an instance of the class by specifying the path of the file that you want to read or write. For example, to read data from a CSV file, you can create an instance of the `FileManager` class and call the `read()` method, as shown below:

```python
fm = FileManager('data.csv')
data = fm.read()
```

To write data to a file, you can create an instance of the `FileManager` class, and call the `write()` method, as shown below:

```python
fm = FileManager('data.xlsx')
fm.write(data_to_write_to_file, add_date_to_filename=True)
```

The `write()` method takes two arguments: `data_to_write_to_file`, which is the data that you want to write to the file, and `add_date_to_filename`, which is a Boolean value that determines whether to add the current date and time to the file name. 

### Supported File Types

The `file_manager` module supports the following file types and extensions:

- Data Table: CSV (.csv), JSON (.json), Excel (.xlsx, .xls)
- Image: PNG (.png), JPG (.jpg), Bitmap (.bmp), GIF (.gif), TIFF (.tiff), WebP (.webp), PPM (.ppm)
- Video: mp4 (.mp4), avi (.avi), wmv (.wmv), flv (.flv), mkv (.mkv), ogv (.ogv), mpeg (.mpeg), mov (.mov)
- Audio: mp3 (.mp3), wav (.wav), aac (.aac), flac (.flac), aiff (.aiff), ogg (.ogg)
- Text: Microsoft Word (.doc, .docx)

### Class Methods

The `FileManager` class has the following methods:

#### `__init__(self, filepath)`

The constructor method for the `FileManager` class. It takes in the `filepath` argument, which is the path to the file to be read or written.

#### `read(self)`

Reads the file and returns its contents. The returned object is dependent on the file type.

#### `write(self, data_to_write_to_file, add_date_to_filename=False)`

Writes the given data to the file. The `data_to_write_to_file` argument is the data that you want to write to the file, and `add_date_to_filename` is a Boolean value that determines whether to add the current date and time to the file name.

#### `add_date(self)`

Appends the current date and time to the file name.

#### `read_data_table(self)`

Reads a table from a CSV, JSON, or Excel file and returns it as a pandas DataFrame.

#### `write_data_table(self, data_to_write_to_file)`

Writes a pandas DataFrame to a CSV, JSON, or Excel file.

#### `read_img(self)`

Reads an image file and returns it as a PIL Image object.

#### `write_img(self, data_to_write_to_file)`

Writes a PIL Image object to an image file.

#### `read_video(self)`

Reads a video file and returns it as a moviepy.VideoFileClip object.

#### `write_video(self, data_to_write_to_file)`

Writes a moviepy.VideoFileClip object to a video file.

#### `read_audio(self)`

Reads an audio file and returns an audio object.

#### `write_audio(self, data_to_write_to_file)`

Writes an audio object to an audio file. The audio file output is determined by the extension of the input filepath argument in the class constructor.

#### `read_text(self)`

Reads a Microsoft Word file and returns a .docx.Document object.

#### `write_text(self, data_to_write_to_file)`

Takes a python Document object and saves it to the specified path.


## pyrus.web