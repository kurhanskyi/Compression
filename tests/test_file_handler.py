import unittest
import os
from utils.file_handler import FileHandler


def test_write_and_read_file(self):
    FileHandler.write_file(self.test_file, self.test_data)
    read_data = FileHandler.read_file(self.test_file)
    self.assertEqual(read_data, self.test_data)

def test_get_file_size(self):
    FileHandler.write_file(self.test_file, self.test_data)
    size = FileHandler.get_file_size(self.test_file)
    self.assertEqual(size, len(self.test_data))
def test_delete_file(self):
    FileHandler.write_file(self.test_file, self.test_data)
    FileHandler.delete_file(self.test_file)
    self.assertFalse(os.path.exists(self.test_file))

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

if __name__ == '__main__':
    unittest.main()
