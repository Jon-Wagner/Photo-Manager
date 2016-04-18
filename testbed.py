import sqlite3 as lite

'''
# this is all just being retained for later. ugly comment is ugly
import argparse as ap

parser = ap.ArgumentParser()
parser.add_argument('-f', '--filepath', nargs = '?', default = 'test.db', help = 'use the specified csv file as the database')
args = parser.parse_args()
# filepath will be in args.filepath
'''

'''
A short implementation of a photo manager, to be used as a testbed for data handling and ui.
All using of data should be seperate from any actual IO. Goal is to be database agnostic for future use
'''
class TestBed:
    db_connection = None
    db_cursor = None

    def __init__(self, db_path):
        self.db_connection = lite.connect(db_path)
        with self.db_connection:
            self.db_cursor = self.db_connection.cursor()

    def create_table(self):
        self.db_cursor.execute("CREATE TABLE Photos (Id INTEGER PRIMARY KEY, File_Path Text, People TEXT DEFAULT 'unknown', \
                                                      Face_Locations TEXT DEFAULT '', Animals TEXT DEFAULT 'unknown', \
                                                      Geographic_Location TEXT DEFAULT 'unknown')")

    def insert_photo(self, photo_to_insert):
        self.db_cursor.execute('INSERT INTO Photos VALUES (?,?,?,?,?,?)', photo_to_insert.get_insertable())

    # TODO: return photos, not rows
    # TODO: create one of these for each column
    def select_name(self, name):
        self.db_cursor.execute('SELECT id FROM Photos WHERE People = ?', name)
        ids = self.db_cursor.fetchall()

    def change_photo(self, photo_to_change):
        photo_to_change.get_insertable()