# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    group = Group(name="group1", header="text1", footer="text2")
    old_groups = app.group.get_groups_list()
    app.group.create(group)

    assert app.group.count() == len(old_groups) + 1

    new_groups = app.group.get_groups_list()
    old_groups.append(group)

    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)


def test_empty_group(app):
    group = Group(name="", header="", footer="")
    old_groups = app.group.get_groups_list()
    app.group.create(group)
    new_groups = app.group.get_groups_list()

    assert len(new_groups) == len(old_groups) + 1

    old_groups.append(group)

    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)
