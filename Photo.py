class Photo():
    data = {'Id': None, 'Filepath': '', 'People': [], 'Face_Locations': {}, 'Animals': [], 'Geographic_Location': ''}
    labels = ['Id', 'Filepath', 'People', 'Face_Locations', 'Animals', 'Geographic_Location']

    def __init__(self, photo_data):
        if type(photo_data) == 'Dict':
            self.create_from_dict(photo_data)
        elif type(photo_data) == 'String':
            self.create_from_string(photo_data)
        else:
            return

    # for each label?
    def add_tag(self, label, value):
        if label == 'People' or label == 'Animals':
            self.data[label].extend(value)
        elif label == 'Face_Locations':
            self.data[label].update(value)
        else:
            self.data[label] = value

    def to_dict(self):
        return self.data

    def to_string(self):
        return

    def create_from_string(self):
        return

    def create_from_dict(self, row_dict):
        self.data = row_dict