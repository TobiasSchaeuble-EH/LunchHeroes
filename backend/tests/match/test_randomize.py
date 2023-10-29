from lunchheros.match._randomize import _randomize_groups


def test_randomize_groups():
    """Test randomize groups."""
    groupsize = 4
    # make list of 21 users with string id
    users = [str(i) for i in range(21)]
    # randomize groups
    groups = _randomize_groups(groupsize, users)
    print(groups)
    # check that all groups are at least 2 users
    assert all(len(group) >= 2 for group in groups)
    # check that all groups are at most 4 users
    assert all(len(group) <= groupsize + groupsize for group in groups)
