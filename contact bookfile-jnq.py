class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def get_details(self):
        return f"Name: {self.name}, Phone: {self.phone}"

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        self.contacts[contact.name] = contact

    def get_contact(self, name):
        if name in self.contacts:
            return self.contacts[name].get_details()
        else:
            return "Contact not found"

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

contact_book = ContactBook()
contact_book.add_contact(Contact("John Doe", "123-4567"))
contact_book.add_contact(Contact("Jane Doe", "234-5678"))

print(contact_book.get_contact("John Doe")) # Output: Name: John Doe, Phone: 123-4567
print(contact_book.get_contact("Jane Doe")) # Output: Name: Jane Doe, Phone: 234-5678
print(contact_book.get_contact("Unknown")) # Output: Contact not found

contact_book.remove_contact("John Doe")
print(contact_book.get_contact("John Doe")) # Output: Contact not found