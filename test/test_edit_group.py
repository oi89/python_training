import random

from model.group import Group


def test_edit_random_group_name(app, db, check_ui):
    new_group = Group(name='group1-edit')

    if len(db.get_groups_list()) == 0:
        app.group.create(Group(name='group for edit'))

    old_groups = db.get_groups_list()
    group_to_edit = random.choice(old_groups)
    app.group.edit_group_by_id(group_to_edit.id, new_group)

    assert app.group.count() == len(old_groups)

    # change group_to_edit to new_group in old_groups list for compare
    map(lambda group: new_group, filter(lambda group: group == group_to_edit, old_groups))
    new_groups = db.get_groups_list()

    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)

    if check_ui:
        sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)


def test_edit_random_group_header(app, db, check_ui):
    new_group = Group(header='text1-edit')

    if len(db.get_groups_list()) == 0:
        app.group.create(Group(header='group for edit'))

    old_groups = db.get_groups_list()
    group_to_edit = random.choice(old_groups)
    app.group.edit_group_by_id(group_to_edit.id, new_group)

    assert app.group.count() == len(old_groups)

    # change group_to_edit to new_group in old_groups list for compare
    map(lambda group: new_group, filter(lambda group: group == group_to_edit, old_groups))
    new_groups = db.get_groups_list()

    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)

    if check_ui:
        sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)


def test_edit_random_group_footer(app, db, check_ui):
    new_group = Group(footer='text2-edit')

    if len(db.get_groups_list()) == 0:
        app.group.create(Group(footer='group for edit'))

    old_groups = db.get_groups_list()
    group_to_edit = random.choice(old_groups)
    app.group.edit_group_by_id(group_to_edit.id, new_group)
    # app.group.edit_first(Group(footer='text2-edit'))

    assert app.group.count() == len(old_groups)

    # change group_to_edit to new_group in old_groups list for compare
    map(lambda group: new_group, filter(lambda group: group == group_to_edit, old_groups))
    new_groups = db.get_groups_list()

    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)

    if check_ui:
        sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)
