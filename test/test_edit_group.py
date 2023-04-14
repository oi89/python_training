from model.group import Group


def test_edit_first_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name='group1-edit'))
    app.session.logout()

def test_edit_first_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(header='text1-edit'))
    app.session.logout()

def test_edit_first_group_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(footer='text2-edit'))
    app.session.logout()
