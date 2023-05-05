# -*- coding: utf-8 -*-
import pytest

from model.group import Group
# we can change what to import - constants or random values
from data.add_group import constant as test_data


@pytest.mark.parametrize("group", test_data, ids=[repr(x) for x in test_data])
def test_add_group(app, group):
    old_groups = app.group.get_groups_list()
    app.group.create(group)

    assert app.group.count() == len(old_groups) + 1

    new_groups = app.group.get_groups_list()
    old_groups.append(group)

    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)
