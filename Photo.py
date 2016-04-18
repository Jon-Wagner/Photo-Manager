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

    def add_tag(self, label, value):
        if label == 'filepath':
            self.filepath = value
        elif label == 'people':
            self.people.extend(value)
        elif label == 'face location':
            for val in value:
                if val[0] in self.people:
                    self.face_locations.append(val)
                else:
                    # TODO: this should provide a clear failure message
                    return
        elif label == 'animals':
            self.animals.extend(value)
        elif label == 'geographic location':
            self.geographic_location = value