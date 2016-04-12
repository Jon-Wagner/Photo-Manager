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

    def create_table(self,  typed_columns):
        self.db_cursor.execute("CREATE TABLE Photos (" + typed_columns + ")")

    def insert_column(self, typed_column, default_value):
        self.db_cursor.execute("ALTER TABLE Photos ADD COLUMN " + typed_column + " DEFAULT '" + default_value + "'")

    def insert_photo(self, row_values):
        self.db_cursor.execute("INSERT INTO Photos VALUES ('" + row_values + "')")

    # this may be vulnerable to SQL injection, column and value should be sanitized
    def select_photo(self, typed_column, value):
        self.db_cursor.execute("SELECT * FROM Photos WHERE " + typed_column + " = '" + value + "'")
        return self.db_cursor.fetchall()

    def change_value(self, match_column, match_value, change_column, change_value):
        self.db_cursor.execute("UPDATE Photos SET " + change_column + " = '" + change_value + "' WHERE " + match_column + " = '" + match_value + "'")

    def sanitize_string(self, unsanitized_string):
        sanitized_string = ''

        return sanitized_string

    def kill(self):
        self.db_cursor.close()