from model.group import Group


def test_edit_first_group_name(app):
    app.group.edit_first(Group(name='group1-edit'))

def test_edit_first_group_header(app):
    app.group.edit_first(Group(header='text1-edit'))

def test_edit_first_group_footer(app):
    app.group.edit_first(Group(footer='text2-edit'))
