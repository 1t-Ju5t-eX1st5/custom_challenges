def generate_random_numbers(num_count: int, min: float | int, max: float | int) -> list:
    from random import randint
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

response = generate_random_numbers(50, 1, 250)
print(response)
print(max(response))