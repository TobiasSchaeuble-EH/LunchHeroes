import random

from lunchheros.db.dbFetcher import parse_user_id_tolist
from lunchheros import GROUP_SIZE


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

    # Calculate the number of groups needed
    num_groups = len(users) // group_size

    # Calculate the number of users that will be left alone
    remaining_users = len(users) % group_size

    # Create the groups
    groups = []
    for i in range(num_groups):
        group = users[i * group_size : (i + 1) * group_size]
        groups.append(group)

    # Distribute the remaining users across the groups
    for i in range(remaining_users):
        groups[i].append(users[num_groups * group_size + i])

    return groups


def matching(userids):

    # convert userids to list
    userids = parse_user_id_tolist(userids)
    # group size
    groupsize = GROUP_SIZE
    # randomize the groups
    groups = _randomize_groups(groupsize, userids)
    # return the groups
    return groups



