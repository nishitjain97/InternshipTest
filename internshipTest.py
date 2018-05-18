def read_from_file(file_name):
    """ Reads data from file and convert into usable form. Returns a tuple of the form (numberOfInputs, inputValue) """

    data_list = []

    # Using 'with' closes file properly, even if error occurs
    with open(file_name, 'r') as file:
        for line in file.readlines():
            line = line.strip('\n')
            data_list.append(int(line))

    return (data_list[0], data_list[1:])

def battle(position, health, injuries, monkey_list):
    """
        Starts from current position to recursively defeat monkeys. Min_health and Max_injuries are
        exit conditions from the recursion.
    """

    # Reduce health and multiply injuries
    health = health - monkey_list[position]
    injuries = injuries * monkey_list[position]

    if health < min_health or injuries > max_injuries or position == N-1:
        return 0
    else:
        return 1 + battle(position+1, health, injuries, monkey_list)

# Number of inputs and input data
(N, monkey_list) = read_from_file('input.txt')

# Initial setup
initial_health = 2000
min_health = 1

injuries = 1
max_injuries = 1000000

max_defeated = 0

# Dynamic programming
defeat_storage = {}

for i in range(N):
    # Find for every position
    defeated_from_current_position = battle(i, initial_health, injuries, monkey_list)
    defeat_storage[i] = defeated_from_current_position

    if defeated_from_current_position > max_defeated:
        max_defeated = defeated_from_current_position
        position = i+1

print(max_defeated)

count = 0

for i in defeat_storage.keys():
    if defeat_storage[i] == max_defeated:
        count += 1

print(count)