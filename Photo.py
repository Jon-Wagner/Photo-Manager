class Photo():
    id = -1
    filepath = ''
    people = []
    face_locations = {'': (-1,-1,-1,-1)}
    animals = {}
    geographic_location = ''

    def __init__(self, id, filepath, people, face_locations, animals, geographic_location):
        self.id = id
        self.filepath = filepath
        self.people = people
        self.face_locations = face_locations
        self.animals = animals
        self.geographic_location = geographic_location

    def add_tag(self, tag_label, tag_value):
        # can either do if ... elif ... else or
        # some sort of function and then dictionary based shenenagins