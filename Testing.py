import unittest
from TestBed import TestBed

'''
TODO
-: test passes
+: code is no longer ugly

- store a photo to the db
- load a photo from the db
display a photo
- add column for a tag to the db
- add tags to a photo
sanitize inputs for every method
'''

class TestPhotoManager(unittest.TestCase):
    photo_manager = None
    test_string_1 = 'test.png'
    test_string_2 = 'other_test.png'
    test_default_location = 'nowhere'
    test_alternate_location = 'somewhere'

    def setUp(self):
        self.photo_manager = TestBed(':memory:')
        self.photo_manager.create_table("File_Name TEXT")
        self.photo_manager.insert_photo(self.test_string_1)

    def tearDown(self):
        self.photo_manager.kill()

    def test_select_photo(self):
        self.photo_manager.insert_photo(self.test_string_2)
        tmp = self.photo_manager.select_photo('File_Name',self.test_string_1)
        self.assertEqual(tmp[0][0], self.test_string_1)
        self.assertNotEqual(tmp[0][0], self.test_string_2)

    def test_insert_column(self):
        self.photo_manager.insert_photo(self.test_string_1)
        self.photo_manager.insert_column("Geographic_Location TEXT", self.test_default_location)
        tmp = self.photo_manager.select_photo('File_Name',self.test_string_1)
        self.assertEqual(tmp[0][1], self.test_default_location)

    # need to do something about determining how to handle arbitrary data types in columns instead of assuming everything is a string
    def test_selecting_on_second_col(self):
        self.photo_manager.insert_column("Geographic_Location TEXT", self.test_default_location)
        self.photo_manager.insert_photo(self.test_string_2 + "', '" + self.test_alternate_location)
        tmp = self.photo_manager.select_photo('Geographic_Location', self.test_default_location)
        self.assertEqual(tmp[0][1], self.test_default_location)
        self.assertEqual(tmp[0][0], self.test_string_1)

    def test_changing_a_value(self):
        self.photo_manager.insert_column("Geographic_Location TEXT", self.test_default_location)
        self.photo_manager.change_value('File_Name', self.test_string_1, 'Geographic_Location', self.test_alternate_location)
        tmp = self.photo_manager.select_photo('Geographic_Location', self.test_alternate_location)
        self.assertEqual(tmp[0][1], self.test_alternate_location)

if __name__  == '__main__':
    unittest.main()