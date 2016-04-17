class Photo():
    filepath = ''
    tags = {}
    
    def __init__(self, filepath, tags):
        self.filepath = filepath
        self.tags = tags

    def add_tag(self, tag_label, tag_value):
        self.tags