from model.group import Group


# parameter json_groups means that we will get test data from file data.groups.json
def test_add_group(app, db, json_groups, check_ui):
    group = json_groups

    old_groups = db.get_groups_list()
    app.group.create(group)

    new_groups = db.get_groups_list()
    old_groups.append(group)

    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)

    if check_ui:
        sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)
