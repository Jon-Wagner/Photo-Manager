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
    
    def __init__(self, filepath):
        self.db_connection = lite.connect(filepath)
    
        
    '''
    def 
        with db_connection:  
            db_cursor = db_connection.cursor()    
            db_cursor.execute('SELECT SQLITE_VERSION()')
            
            data = db_cursor.fetchone()
            
            print("SQLite version: %s" % data)                
    '''