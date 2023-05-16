"""
This module contains unit tests for the FileManager class in file_manager.py.

The tests cover basic functionality such as reading and writing files, 
handling file types, and handling errors.
"""

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pyrus.file_manager import FileManager
import tempfile
import unittest
import curses
from PIL import Image
import pandas as pd

class TestFileManager(unittest.TestCase):

    def setUp(self):
        self.stdscr = curses.initscr()
        self.temp_dir = tempfile.TemporaryDirectory()
        self.filepath = os.path.join(self.temp_dir.name, "test.csv")
        self.file_manager = FileManager(self.filepath)
        
    def tearDown(self):
        self.temp_dir.cleanup()
        curses.endwin()

    def test_file_read_write(self):
        data = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
        
        with self.subTest(msg="Test reading and writing CSV file"):
            self.file_manager.write(data)
            self.assertTrue(os.path.exists(self.filepath))
            data_read = pd.read_csv(self.filepath)
            pd.testing.assert_frame_equal(data, data_read)

        with self.subTest(msg="Test reading and writing JSON file"):
            self.filepath = os.path.join(self.temp_dir.name, "test.json")
            self.file_manager = FileManager(self.filepath)
            self.file_manager.write(data)
            self.assertTrue(os.path.exists(self.filepath))
            data_read = pd.read_json(self.filepath)
            pd.testing.assert_frame_equal(data, data_read)

        with self.subTest(msg="Test reading and writing Excel file"):
            self.filepath = os.path.join(self.temp_dir.name, "test.xlsx")
            self.file_manager = FileManager(self.filepath)
            self.file_manager.write(data)
            self.assertTrue(os.path.exists(self.filepath))
            data_read = pd.read_excel(self.filepath)
            pd.testing.assert_frame_equal(data, data_read)

        with self.subTest(msg="Test reading and writing PNG image file"):
            self.filepath = os.path.join(self.temp_dir.name, "test.png")
            self.file_manager = FileManager(self.filepath)
            img = Image.new(mode="RGB", size=(100, 100), color="red")
            self.file_manager.write(img)
            self.assertTrue(os.path.exists(self.filepath))
            img_read = Image.open(self.filepath)
            self.assertEqual(img.size, img_read.size)

        with self.subTest(msg="Test reading and writing MP4 video file"):
            self.filepath = os.path.join(self.temp_dir.name, "test.mp4")
            self.file_manager = FileManager(self.filepath)
            with self.assertRaises(NotImplementedError):
                self.file_manager.write("data")

        with self.subTest(msg="Test reading and writing MP3 audio file"):
            self.filepath = os.path.join(self.temp_dir.name, "test.mp3")
            self.file_manager = FileManager(self.filepath)
            with self.assertRaises(NotImplementedError):
                self.file_manager.write("data")

        with self.subTest(msg="Test reading and writing Word file"):
            self.filepath = os.path.join(self.temp_dir.name, "test.docx")
            self.file_manager = FileManager(self.filepath)
            with self.assertRaises(NotImplementedError):
                self.file_manager.write("data")

    def test_add_date(self):
        filename = os.path.basename(self.filepath)
        self.file_manager = FileManager(filename)
        with self.subTest(msg="Test adding date to content"):
            self.file_manager.write(filename, add_date_to_filename=True)
            
            with open(self.file_manager.filepath, "r", encoding='UTF-8') as f:
                content = f.read()
                self.assertIn(self.file_manager.date_added, content)
                date_added = True

        with self.subTest(msg="Test not adding date to content"):
            self.file_manager.write(filename, date_added)
            with open(self.file_manager.filepath, "r") as f:
                content = f.read()
                self.assertNotIn(self.file_manager.date_added, content)
                self.assertTrue(date_added)

if __name__ == '__main__':
    curses.wrapper(unittest.main())
