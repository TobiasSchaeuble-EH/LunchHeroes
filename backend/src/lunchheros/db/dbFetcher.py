
import numpy as np
import pandas as pd
import random
import json
import os 

def filter_data(data):
    print("get_encoded_data")
    return matching(data)
    
def matching(userids):

    # convert userids to list
    userids = parse_user_id_tolist(userids)
    # group size
    groupsize = 4
    # randomize the groups
    groups = _randomize_groups(groupsize, userids)
    # return the groups
    return groups


def _randomize_groups(group_size: int, users: list[str]) -> list[list]:
    """Randomize the groups of users.

      Makes groups of size ``group_size`` from the list of users ``users``.
      If the number of users is not a multiple of ``group_size``, the remaining
      users will be distributed randomly across the groups.

    Args:
        group_size: size of the groups
        users: list of users id
    Returns:
        A list of lists, each representing a group of users
    """

    # Shuffle the users randomly
    random.shuffle(users)

    print(f"users: {users}")
    print(f"len(users): {len(users)}")

    if len(users) < group_size:
        return [users]

    # Calculate the number of groups needed
    num_groups = len(users) // group_size

    print(f"num_groups: {num_groups}")

    # Calculate the number of users that will be left alone
    remaining_users = len(users) % group_size

    print(f"remaining_users: {remaining_users}")

    # Create the groups
    groups = []
    for i in range(num_groups):
        group = users[i * group_size : (i + 1) * group_size]
        groups.append(group)
        print(f"groups: {groups}")

    # get the number of groups
    num_groups = len(groups)

    # Distribute the remaining users across the groups
    #for i in range(remaining_users):
    #    groups[i].append(users[num_groups * group_size + i])

    # Distribute the remaining users across the groups
    for i in range(remaining_users):
        groups[i % num_groups].append(users[num_groups * group_size + i])

    return groups


def parse_user_id_tolist(test_data):
    
   
    parsed_string = str(test_data)
    
    parsed_string = parsed_string.replace("'", '"')

    data = json.loads(parsed_string)

    # Extract the id values into a python list
    ids = [x['id'] for x in data]

    # Convert the python list to a numpy array
    numpy_array = np.array(ids).tolist()

    return numpy_array
