class Vote():

    def __init__(self, image_id='asf2', sub_id='my-user-1234', value=1):
        self.image_id = image_id
        self.sub_id = sub_id
        self.value = value

##Gets
    def get_value(self):
        return self.value

    def get_sub_id(self):
        return self.sub_id

    def get_image_id(self):
        return self.image_id

##Sets
    def set_value(self, value):
        self.value = value

    def set_sub_id(self, sub_id):
        self.sub_id = sub_id

    def set_image_id(self, image_id):
        self.image_id = image_id