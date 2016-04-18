import unittest
from TestBed import TestBed

'''
TODO
-: test passes
+: code is no longer ugly

Photo:
create a photo with values
add new values
don't overwrite existing values
confirm overwriting existing values
create from a row
export to a row
export to displayable

TestBed:
create a table
insert a photo
select a photo
change values for a photo
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

class TestPhoto(unittest.TestCase):

if __name__  == '__main__':
    unittest.main()