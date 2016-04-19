import unittest
from TestBed import TestBed
from Photo import Photo

"""
TODO
-: test passes
+: code is no longer ugly

Photo:
- create a photo with values
- add new values
add new values without being a clusterfuck of lists
don't overwrite existing values
confirm overwriting existing values
- create from a row
export to a row
export to displayable
add a value containing punctuation (ex: Foo's dog)

TestBed:
create a table
insert a photo
select a photo
change values for a photo
"""

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

class TestPhoto(unittest.TestCase):
    test_row = {'Id': 314, 'Filepath': 'test.png', 'People': ['Foo', 'Bar'], 'Face_Locations': {'Foo': (10,10,10,10), 'Bar': (30,10,10,10)}, \
                'Animals': [], 'Geographic_Location': 'unknown'}
    test_photo = None

    def setUp(self):
        self.test_photo = Photo(self.test_row)

    def test_create_photo(self):
        for x in self.test_row.keys():
            self.assertEqual(self.test_photo.export_dictionary()[x], self.test_row[x])

    def test_change_a_photo_value(self):
        self.test_photo.add_tag('Animals', ['Foos Dog'])
        self.assertEqual(self.test_photo.export_dictionary()['Animals'], ['Foos Dog'])

    def test_export_dictionary(self):
        self.assertEqual(self.test_photo.export_dictionary(), self.test_row)

if __name__  == '__main__':
    unittest.main()