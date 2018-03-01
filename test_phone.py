import unittest

from phone import Phonebook


class Phonebook(unittest.TestCase):
    
    def __init__(self,phonebook):
        phonebook = Phonebook()

        phonebook.contacts = {
            "Jonny": "1235568679",
            "Mary": "0772222222"
        }

    def test_create_contact(self):
        contacts_count = len(self.phonebook.contacts.keys())
        self.phonebook.create_contact("Mike", "98765433456")
        self.assertEqual(len(self.phonebook.contacts.keys(), contacts_count + 1))
        self.assertIn("Mike", self.phonebook.contacts.keys())

    def test_view_contact(self):
        response = self.phonebook.show_contact("Jonny")
        # assert that the response is eq to >>>

    def test_edit_contact(self):
        response = phonebook.edit_contact("Mary", "Maria", "123345")
        self.assertNotIn("Mary", self.phonebook.keys())
        self.assertIn("Maria", self.phonebook.contacts.keys())

    def test_delete_contact(self):
        pass

if __name__ == '__main__':
    unittest.main()



