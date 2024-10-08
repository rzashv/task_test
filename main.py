import argparse

def reader(file: str) -> list:
    """
    Opens the test file

    Args:
        file (str)): The file with all of the information about the users

    Returns:
        list: A list consisting of strings with information about the users
    """
    if isinstance(file, str) and file[-4:] == '.txt':
        try:
            with open(file, 'r') as f:
                lines = f.readlines()
                return lines
        except FileNotFoundError:
            return None
    else:
        print('Incorrect data type', file)
        return None


def splitter(line: str) -> list:
    """
    Sets up the necessary input lines

    Args:
        line (str): A string with a separator 

    Returns:
        list: A list consisting of string objects 
        If the data is incorrect, returns None
    """
    if isinstance(line, str):
        new_line = line.strip().split(':')
        if len(new_line) == 5:
            new_line.pop(0)
            new_line.pop(-1)
            return new_line
        else:
            print('Incorrect line length')
            return None
    else:
        print('Incorrect data type', line)
        return None



def username_generator(line: str) -> str:
    """
    Creates a username based on the set line

    Args:
        line (str): 

    Returns:
        str: 
    """
    global usernames
    new_line = splitter(line)
    if new_line is None:
        return None
    username = ''
    for i in new_line:
        if i != new_line[-1]:
            username += i[:1]
        else:
            username += i

    if len(username) > 8:
        username = username[:8].lower()
    else:
        username = username.lower()

    if username not in usernames:
        usernames[username] = 0
    else:
        usernames[username] += 1
        username = username + str(usernames[username])
    
    return username


def result(output_file: str, input_files: list) -> None:
    """
    Adds the final usernames to a new file

    Args:
        output_file (str): The file with strings with written in usernames
        input_files (list): The given files
    """    
    if isinstance(output_file, str) and output_file[-4:] == '.txt':
        with open(output_file, 'w') as f:
            l = []
            for i in input_files:
                file = reader(i)
                if file is not None:
                    l += file
            lines = []
            for i in l:
                new_line = i.strip().split(':')
                user = username_generator(i)
                if user is None:
                    new_line.insert(1, 'incorrect input data')
                else:
                    new_line.insert(1, user)
                line = ':'.join(new_line) + '\n'
                lines.append(line)
            
            f.writelines(lines)


usernames = {}
if __name__ == '__main__':


    parser = argparse.ArgumentParser(description='Generating usernames from input file')
    parser.add_argument('-o', '--output', required=True, help='Output file')
    parser.add_argument('input_files', nargs='+', help='Input files')

    try:
        args=parser.parse_args()
        result(args.output, args.input_files)

    except:
        parser.print_help()