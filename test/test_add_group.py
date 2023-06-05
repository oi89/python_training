import allure

from model.group import Group


# parameter json_groups means that we will get test data from file data.groups.json
def test_add_group(app, db, json_groups, check_ui):
    group = json_groups

    with allure.step("Given a group list"):
        old_groups = db.get_groups_list()

    with allure.step(f"When add the group {group}"):
        app.group.create(group)

    with allure.step("Then new groups list is equal to old groups list with added group"):
        new_groups = db.get_groups_list()
        old_groups.append(group)

        assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)

        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)
