import pytest
from selene import have
from selene.support.shared import browser


@pytest.fixture
def mobile():
    browser.config.window_width = 320
    browser.config.window_height = 569
    yield
    browser.quit()


@pytest.fixture
def desktop():
    browser.config.window_width = 1366
    browser.config.window_height = 768
    yield
    browser.quit()


def test_mobile(mobile):
    browser.open("https://github.com/")
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))


def test_desktop(desktop):
    browser.open("https://github.com/")
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
