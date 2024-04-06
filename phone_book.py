class PhoneRecord:
    def __init__(self, name, organisation, phone_numbers):
        self.name = name
        self.organisation = organisation
        self.phone_numbers = phone_numbers

    def get_name(self):
        return self.name

    def get_organisation(self):
        return self.organisation

    def get_phone_numbers(self):
        return self.phone_numbers


class HashTableRecord:
    def __init__(self, key, record):
        self.key = key
        self.record = record
        self.next = None

    def get_key(self):
        return self.key

    def get_record(self):
        return self.record

    def get_next(self):
        return self.next

    def set_next(self, nxt):
        self.next = nxt


class PhoneBook:
    HASH_TABLE_SIZE = 263

    def __init__(self):
        self.hash_table = [None] * PhoneBook.HASH_TABLE_SIZE

    def compute_hash(self, string):
        # Implement a hash function for strings
        # You can use Python's built-in hash function or implement a custom one
        hash_value = 0
        for char in string:
            hash_value = (hash_value * 31 + ord(char)) % PhoneBook.HASH_TABLE_SIZE
        return hash_value

    def add_contact(self, record):
        # Implement adding a contact to the phone book
        # You need to compute the hash for the record's name and insert it into the hash table
        name = record.get_name()
        key1 = self.compute_hash(name)
        key2 = self.compute_hash(name.split()[0])  # First name
        key3 = self.compute_hash(name.split()[-1])  # Last name

        # Create HashTableRecord objects for each key
        hash_record1 = HashTableRecord(key1, record)
        hash_record2 = HashTableRecord(key2, record)
        hash_record3 = HashTableRecord(key3, record)

        # Insert the records into the hash table
        self._insert_record(hash_record1)
        self._insert_record(hash_record2)
        self._insert_record(hash_record3)

    def _insert_record(self, hash_record):
        key = hash_record.get_key()
        index = key % PhoneBook.HASH_TABLE_SIZE

        if self.hash_table[index] is None:
            self.hash_table[index] = hash_record
        else:
            current = self.hash_table[index]
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(hash_record)

    def create_phone_record(self, line):
        
        parts = line.strip().split(',')
        name = parts[0]
        organization = parts[-1]
        phone_numbers = parts[1:-1]

        # Create a PhoneRecord object
        phone_record = PhoneRecord(name, organization, phone_numbers)


    def delete_contact(self, search_name):
    # Implement deleting a contact from the phone book using the contact_names set
    # Return True if at least one contact is deleted, False otherwise

    # Convert the search name to lowercase
        search_name = search_name.lower()

        # Check if the search name exists in the contact_names set
        if search_name in self.contact_names:
            # The contact exists, proceed with deletion
            deleted = False

            # Iterate through the hash table slots
            for index in range(PhoneBook.HASH_TABLE_SIZE):
                current = self.hash_table[index]
                prev = None
                while current is not None:
                    contact_name = current.get_record().get_name().lower()

                    # Check if the contact name matches the search name
                    if contact_name == search_name:
                        # Found a matching contact, remove it from the linked list
                        if prev is None:
                            self.hash_table[index] = current.get_next()
                        else:
                            prev.set_next(current.get_next())
                        deleted = True
                    prev = current
                    current = current.get_next()

            return deleted

        # The contact does not exist, return False
        return False

    def fetch_contacts(self, query):
        # Implement fetching contacts based on the query
        # You may need to split the query into words and hash them separately
        # Then, retrieve and merge the records from the appropriate hash table slots
        # Sort and return the merged records
        result = []

        # Create a list of unique PhoneRecord objects
        unique_records = set()

        for word in query.split():
            key = self.compute_hash(word)
            index = key % PhoneBook.HASH_TABLE_SIZE
            current = self.hash_table[index]
            while current is not None:
                unique_records.add(current.get_record())
                current = current.get_next()

        result.extend(list(unique_records))
        result.sort(key=lambda record: record.get_name())
        return result

    def read_records_from_file(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()

        for line in lines:
            # Split the line into name, phone numbers, and organization
            parts = line.strip().split(',')
            name = parts[0]
            organization = parts[-1]
            phone_numbers = parts[1:-1]

            # Create a PhoneRecord object
            phone_record = PhoneRecord(name, organization, phone_numbers)

            # Add the PhoneRecord object to the PhoneBook
            self.add_contact(phone_record)


if __name__ == "__main__":
    phone_book = PhoneBook()

    # Specify the filename from which to read contacts
    filename = "Details_new.txt"

    if PhoneBook.read_records_from_file(filename, phone_book):
        # Perform other operations with the PhoneBook as needed
        pass
    else:
        print("Error reading contacts from the file.")
