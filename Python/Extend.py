def extend_list(lst):
    """
    Appends the integer 10 to the end of the provided list.

    Parameters:
    lst (list): The list to be extended.

    Returns:
    None
    """
    lst.extend([10])

    b = [5,10,15,20]
    extend_list(b)
    print(len(b))  # Output: [5, 10, 15, 20, 10]
