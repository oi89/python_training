# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="group1", header="text1", footer="text2"))

def test_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
