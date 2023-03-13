import os
from selenium.webdriver.support import expected_conditions as EC

import pytest

caps = []
device = None
user = None


def pytest_addoption(parser):
    parser.addoption("--user", action="store", default='master')
    parser.addoption("--device", action="store", default='appium_prod')


def pytest_configure(config):
    global device
    global user
    device = config.getoption('--device')
    user = config.getoption('--user')
    return user, device


@pytest.fixture(scope='session', autouse=True)
def options(request):
    yield request.config.option


@pytest.fixture(scope='session', autouse=True)
def get_user(request):
    env = request.config.getoption("--user")
    return env


@pytest.fixture(scope='session', autouse=True)
def get_device(request):
    env = request.config.getoption("--device")
    return env


pytest_plugins = [
    "api_actions.endpoints",
    "api_actions.api_methods",
    "api_actions.login_api"
]
