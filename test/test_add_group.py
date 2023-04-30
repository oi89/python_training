# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
    # connect letters, numbers, punctuation symbols and space
    # to get more spaces in result string, multiply " " to 10 times
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# create 1 empty group and 5 groups with random names
test_data = [Group(name="", header="", footer="")] + [
    Group(name=random_string("group_", 10), header=random_string("header_", 20), footer=random_string("footer_", 20))
    for i in range(5)
]


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(app, group):
    old_groups = app.group.get_groups_list()
    app.group.create(group)

    assert app.group.count() == len(old_groups) + 1

    new_groups = app.group.get_groups_list()
    old_groups.append(group)

    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)
