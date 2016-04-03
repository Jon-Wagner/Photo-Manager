import unittest
from Photo import Photo

'''
TODO
-: test passes
+: code is no longer ugly

store a photo to the db
load a photo from the db
have a photo object
display a photo
add tags to a photo
'''

class TestPhotoManager(unittest.TestCase):
    def test_create_photo(self):
        photo = Photo('filepath')
        self.assertEquals(photo.filepath, 'filepath')
        
    def test_insert_photo(self):
        self.assertTrue(True)

    def test_select_photo(self):
        self.assertTrue(True)
        
if __name__  == 'main':
    unittest.main()