
def read_data(file_path):
    persons_list = []

    with open(file_path, 'r') as file:

        for line in file.readlines():
            person_tuple = tuple(line.strip().split(','))
            persons_list.append(person_tuple)
    return persons_list