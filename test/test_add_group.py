from model.group import Group


# parameter json_groups means that we will get test data from file data.groups.json
def test_add_group(app, json_groups):
    group = json_groups
    old_groups = app.group.get_groups_list()
    app.group.create(group)

    assert app.group.count() == len(old_groups) + 1

    new_groups = app.group.get_groups_list()
    old_groups.append(group)

    assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)
