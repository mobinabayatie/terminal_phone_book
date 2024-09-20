from Models.contact import Contact


class PhoneBook:
    def __init__(self, contact_list=None):
        if not contact_list:
            self.contact_list = []
        else:
            self.contact_list = contact_list

        self.show_contact_list = self.contact_list.copy()

    def create_contact(self, firstname, lastname, phone):
        new_id = len(self.contact_list) + 1
        new_contact = Contact(new_id, firstname, lastname, phone)

        self.contact_list.append(new_contact)
        self.show_contact_list.append(new_contact)

    def search(self, term):
       self.show_contact_list.clear()
       for contact in self.contact_list:
           if term.upper() in contact.first_name.upper() or term in contact.last_name.upper():
               self.show_contact_list.append(contact)

    def delete_contact(self, id):
        for contact in self.contact_list:
            if contact.id == id:
                self.contact_list.remove(contact)
        self.show_contact_list = self.contact_list.copy()

    def get_contact(self, id):
        for contact in self.contact_list:
            if contact.id == id:
                return contact
