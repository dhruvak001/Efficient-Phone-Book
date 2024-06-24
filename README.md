# Efficient Phone Book System (Python)



This Python script provides an efficient implementation for managing contacts in a phone book using a hash table. It allows adding, deleting, and fetching contacts based on names and organization names. The script reads contact details from a file and populates the phone book accordingly.

Imagine you have a phone book, but it's not a regular one. It's a special phone book where you can save contact information like names, organizations, and phone numbers.</br>
- **Saving Contacts:** You can add people's names, their organizations (like their workplace or school), and one or more phone numbers associated with them.</br>
- **Finding Contacts:** You can search for people's names or parts of their names (such as first name, middle name, last name) to find their contact information.</br>
- **Removing Contacts :** You can also delete someone's contact information if you don't need it anymore.</br>

## **Features:**</br>
- **PhoneRecord Class:** Represents a phone record with attributes for name, organization, and phone numbers.</br>
- **HashTableRecord Class:** Defines a node structure for hash table entries, storing key-value pairs (hash and record).</br>
- **PhoneBook Class:** Implements the phone book functionality, including adding, deleting, and fetching contacts. It utilizes a hash table for efficient storage and retrieval.</br>
- **Compute_hash() Method:** Implements a hash function for generating hash values from strings.</br>
- **add_contact() Method:** Adds a contact to the phone book by computing hashes for the contact's name and inserting them into the hash table.</br>
- **delete_contact() Method:** Deletes a contact from the phone book based on the search name.</br>
- **fetch_contacts() Method:** Retrieves contacts based on a query, splitting the query into words and hashing them to find relevant records.</br>
- **read_records_from_file() Method:** Reads contact details from a file and adds them to the phone book.</br>

## **How to Use:**</br>
- Ensure you have Python installed on your system.</br>
- Download the script (phone_book_management.py) to your local machine.</br>
- Prepare a text file (Details_new.txt) containing contact details in the format: Name,PhoneNumber1, PhoneNumber2...Organization.</br>
- Modify the filename variable in the script to match the path to your contact details file.</br>
- The script will read the contact details from the file, populate the phone book, and perform other operations as needed.</br>

## **Note:**</br>
- This script provides a basic implementation of a phone book management system and can be extended for additional features.</br>
- The hash function implemented in compute_hash() can be customized or replaced with a more suitable one based on specific requirements.</br>
- For any issues or suggestions, please feel free to raise them in the repository.</br>
