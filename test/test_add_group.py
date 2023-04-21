# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_groups_list()
    app.group.create(Group(name="group1", header="text1", footer="text2"))
    new_groups = app.group.get_groups_list()

    assert len(new_groups) == len(old_groups) + 1


def test_empty_group(app):
    old_groups = app.group.get_groups_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_groups_list()

    assert len(new_groups) == len(old_groups) + 1
