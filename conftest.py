import pytest
import json
import os.path
import importlib
import jsonpickle

from fixture.application import Application
from fixture.db import DbFixture

fixture = None
target = None


def load_config(file):
    global target

    if target is None:
        # get directory's name of current file "conftest.py" and combine it with name of config file
        file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(file) as config_file:
            target = json.load(config_file)

    return target


@pytest.fixture
def app(request):
    global fixture

    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))["web"]

    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])

    fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])

    return fixture


@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))["db"]
    db_fixture = DbFixture(host=db_config["host"], name=db_config["name"], user=db_config["user"],
                           password=db_config["password"])

    def fin():
        db_fixture.destroy()

    request.addfinalizer(fin)
    return db_fixture


@pytest.fixture
def check_ui(request):
    # return True if parameter exists or False
    return request.config.getoption("--check_ui")


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


# pytest hook for add parameter to launch tests
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    # config file
    parser.addoption("--target", action="store", default="target.json")
    # store_true - value of option will be True if it exists, False if it doesn't exist
    parser.addoption("--check_ui", action="store_true")


# pytest hook for parametrization (called when collect a test method)
def pytest_generate_tests(metafunc):
    # go through all parameters of test method
    for param in metafunc.fixturenames:
        if param.startswith("data_"):
            # load test data from module removing "test_" (for example, "test_groups" -> "groups")
            test_data = load_from_module(param[5:])
            # add parametrization to test method
            metafunc.parametrize(param, test_data, ids=[str(x) for x in test_data])
        elif param.startswith("json_"):
            # load test data from file removing "json_" (for example, "json_groups" -> "groups")
            test_data = load_from_json(param[5:])
            # add parametrization to test method
            metafunc.parametrize(param, test_data, ids=[str(x) for x in test_data])


def load_from_module(module):
    # import module by name from data package and return test_data variable
    return importlib.import_module(f"data.{module}").test_data


def load_from_json(filename):
    # read json file by name
    file = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"data/{filename}.json")
    with open(file) as f:
        # decode json to original object
        return jsonpickle.decode(f.read())
