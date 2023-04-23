from model.group import Group


def test_edit_first_group_name(app):
    group = Group(name='group1-edit')

    if app.group.count() == 0:
        app.group.create(Group(name='group for edit'))

    old_groups = app.group.get_groups_list()
    app.group.edit_first(group)

    assert app.group.count() == len(old_groups)

    group.id = old_groups[0].id
    old_groups[0] = group
    new_groups = app.group.get_groups_list()

    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)

def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header='group for edit'))

    old_groups = app.group.get_groups_list()
    app.group.edit_first(Group(header='text1-edit'))
    new_groups = app.group.get_groups_list()

    assert len(new_groups) == len(old_groups)

def test_edit_first_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer='group for edit'))

    old_groups = app.group.get_groups_list()
    app.group.edit_first(Group(footer='text2-edit'))
    new_groups = app.group.get_groups_list()

    assert len(new_groups) == len(old_groups)
