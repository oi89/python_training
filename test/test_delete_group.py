import random

from model.group import Group


def test_delete_some_random_group(app, db):
    if len(db.get_groups_list()) == 0:
        app.group.create(Group(name='group for delete'))

    old_groups = db.get_groups_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)

    assert app.group.count() == len(old_groups) - 1

    new_groups = db.get_groups_list()
    # remove element of the original list and compare lists
    old_groups.remove(group)
    assert new_groups == old_groups
