# Portfolio Assignment 1: Text Processing with Python
# Houston Holman
# 2/3/22

import sys
import pathlib
import re
import pickle


class Person:
    # Class that stores basic information about a person

    def __init__(self, last, first, mi, person_id, phone):
        # Basic constructor for Person class

        self.last = last
        self.first = first
        self.mi = mi
        self.id = person_id
        self.phone = phone

    def display(self):
        # Prints a person's information in a readable format to the console

        print('Employee id: ' + self.id)
        print('\t' + self.first + ' ' + self.mi + ' ' + self.last)
        print('\t' + self.phone)


def read_file(filepath):
    """Converts a text file into a string object
    Args:
        filepath (string): relative path of text file
    Returns:
        string: contents of text file
    """

    with open(pathlib.Path.cwd().joinpath(filepath), 'r') as f:
        text_in = f.read()
    return text_in


def make_capital_case(name):
    """Modifies input string to be capital case
    Args:
        name (string): input string to be made capital case
    Returns:
        string: modified version of name with first letter uppercase with the rest lowercase
    """

    modified_name = name.lower()
    return modified_name[0].upper() + modified_name[1:]


def modify_middle(middle):
    """Modifies input char to be capital or 'X' if no char provided
    Args:
        middle (char): input char to be modified
    Returns:
        string: modified version of middle that is either uppercased or 'X' if middle is blank
    """

    return 'X' if middle == '' else middle.upper()


def modify_id(person_id):
    """Modifies input string to be in the correct format for an id.
       Prompts user to enter correct string if the input's format is invalid.
    Args:
        person_id (string): input string to be modified
    Returns:
        string: modified version of person_id in the correct format (XX1234)
    """

    while not re.search('^[a-zA-Z]{2}[0-9]{4}$', person_id):
        print('ID invalid: ' + person_id)
        print('ID is two letters followed by 4 digits')
        person_id = input('Please enter a valid id: ')
    return person_id.upper()


def modify_phone(phone):
    """Modifies input string to be in the correct format for a phone number.
       Prompts user to enter correct string if the input's format is invalid.
    Args:
        phone (string): input string to be modified
    Returns:
        string: modified version of phone in the correct format (123-456-7890)
    """
    if re.search('^([0-9]{10})$', phone):
        return phone[0:3] + '-' + phone[3:6] + '-' + phone[6:]
    if re.search('^([0-9]{3}[\\-. ]){2}[0-9]{4}$', phone):
        return phone[0:3] + '-' + phone[4:7] + '-' + phone[8:]
    while not re.search('^([0-9]{3}-){2}[0-9]{4}$', phone):
        print('Phone '+phone+' is invalid')
        print('Enter phone number in form 123-456-7890')
        phone = input('Enter phone number: ')
    return phone


def process_text(file_text):
    """Processes a string filled with outdated person data to fix inconsistencies
       and bad formatting.
    Args:
        file_text (string): text containing people's information
    Returns:
        dict<Person>: dictionary of person of objects with corrected fields
    """

    people_dict = {}
    lines = file_text.split('\n')
    for i in range(len(lines)-1):
        fields = lines[i+1].split(',')

        last = make_capital_case(fields[0])
        first = make_capital_case(fields[1])
        mi = modify_middle(fields[2])
        person_id = modify_id(fields[3])
        phone = modify_phone(fields[4])

        if person_id in people_dict:
            print('ERROR: '+person_id+' is repeated in the input file')
        people_dict[person_id] = Person(last, first, mi, person_id, phone)

    return people_dict


if __name__ == '__main__':
    """Takes in a text file of questionable person data and corrects the formatting.
       Saves the corrected data into a person dictionary stored in a pickle file.
       Data printed to console from pickle file.
    
       sys.argv must contain the filepath to the text file with the person data
    """

    if len(sys.argv) < 2:
        sys.exit('ERROR: filepath must be entered as sysarg')
    else:
        fp = sys.argv[1]
    text = read_file(fp)
    people = process_text(text)

    pickle.dump(people, open('people.p', 'wb'))

    people_in = pickle.load(open('people.p', 'rb'))

    print('Employee list:\n')
    for person in people_in:
        people_in[person].display()
        print()
