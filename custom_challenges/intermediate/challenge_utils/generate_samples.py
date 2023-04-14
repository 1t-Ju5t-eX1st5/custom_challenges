from secrets import choice
from math import inf
from random import randint

def generate_alphabet() -> dict:
    """
    Generates the alphabet in lowercase, uppercase and in both string and list format for use in exercises

    Arguments:
    None

    Returns:
    response (dict (?)) - the generated alphabet for lowercase and uppercase, in string and list format
    """
    lowercase_list, uppercase_list = [], []
    lowercase_string, uppercase_string = "", ""
    for l in range(97, 122):
        lowercase_string += chr(l)
        lowercase_list.append(chr(l))
    for u in range(65, 90):
        uppercase_string += chr(u)
        uppercase_list.append(chr(u))
    response = {
        'list-format': {
            'lowercase': lowercase_list,
            'uppercase': uppercase_list
        },
        'string-format': {
            'lowercase': lowercase_string,
            'uppercase': uppercase_string
        }
    }
    return response


def generate_random_string(string_len: int) -> str:
    """
    Generates a random string with a given length

    Arguments: 
    string_len (int): the length of the random string to be generated

    Returns:
    response (str): generated random string
    """
    alphabet = generate_alphabet()
    selection = alphabet['string-format']['lowercase'] + alphabet['string-format']['uppercase']
    response = ""
    for i in range(string_len):
        response += choice(selection)
    return response

def generate_random_numbers(num_count: int, min: float | int, max: float | int) -> list:
    """
    Generates a list of random numbers

    Arguments:
    num_count (int): length of list (aka how many random numbers to be generated)
    min (float): the lowest possible number that can be generated
    max (float): the highest possible number that can be generated

    Returns:
    response (list): the list of randomly generated numbers
    """
    response = []
    for i in range(num_count):
        response.append(randint(min, max))
    return response