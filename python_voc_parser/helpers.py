
def get_file_lines(file_path):
    """ Function that read a file and return a list of line.

    Function that read a file and return a list of line. Test it to be\
     the fastest way to read lines from a file.

    Args:
        file_path (str): file path to be readed


    Returns:
        (:obj:`list` of :obj:`str`): lines readed from file

    """
    with open(file_path, 'r') as file:
        return file.read().splitlines()
