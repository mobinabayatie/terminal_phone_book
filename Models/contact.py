class Contact:
    def __init__(self,id, firstname, lastname, phone):
        self.id=id
        self.first_name = firstname
        self.last_name = lastname
        self.phone_number = phone

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"

    def update(self, new_firstname, new_lastname, new_phone):
        self.first_name = new_firstname
        self.last_name = new_lastname
        self.phone_number = new_phone

    def call(self):
        pass

    def sms(self, message):
        pass
