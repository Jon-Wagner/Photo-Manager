class Photo():
    id = -1
    filepath = ''
    people = []
    face_locations = {'': (-1,-1,-1,-1)}
    animals = {}
    geographic_location = ''

    def __init__(self, row_dict):
        self.__create__(row_dict['Id'], row_dict['Filepath'], row_dict['People'], row_dict['Face_Locations'], row_dict['Animals'], row_dict['Geographic_Location'])

    def __create__(self, id, filepath, people, face_locations, animals, geographic_location):
        self.id = id
        self.filepath = filepath
        self.people = people
        self.face_locations = face_locations
        self.animals = animals
        self.geographic_location = geographic_location

    def add_tag(self, label, value):
        if label == 'Filepath':
            self.filepath = value
        elif label == 'People':
            self.people.extend(value)
        elif label == 'Face_Locations':
            for val in value:
                if val[0] in self.people:
                    self.face_locations.append(val)
                else:
                    # TODO: this should provide a clear failure message
                    return
        elif label == 'Animals':
            self.animals.extend(value)
        elif label == 'Geographic_Location':
            self.geographic_location = value