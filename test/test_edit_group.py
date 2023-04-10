from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name='group1-edit', header='text1-edit', footer='text2-edit'))
    app.session.logout()
