import allure

from model.group import Group


# get both fixtures from parameters
def test_group_list(app, db):
    with allure.step("Given groups list from web"):
        web_list = app.group.get_groups_list()

    with allure.step("Given groups list from database"):
        # remove spaces from group names
        def clean(group):
            return Group(id=group.id, name=group.name.strip())

        db_list = map(clean, db.get_groups_list())

    with allure.step("Then groups from web page and from database are equal"):
        assert sorted(web_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
