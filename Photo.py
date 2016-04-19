class Photo():
    data = {'Id': None, 'Filepath': '', 'People': [], 'Face_Locations': {}, 'Animals': [], 'Geographic_Location': ''}
    labels = ['Id', 'Filepath', 'People', 'Face_Locations', 'Animals', 'Geographic_Location']

    def __init__(self, row_dict):
        self.data = row_dict

    # for each label?
    def add_tag(self, label, value):
        if label == 'People' or label == 'Animals':
            self.data[label].extend(value)
        elif label == 'Face_Locations':
            self.data[label].update(value)
        else:
            self.data[label] = value

    def export_dictionary(self):
        return self.data
