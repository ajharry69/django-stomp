import os

from django.conf import settings


def pytest_assertrepr_compare(config, op, left, right):
    """
    More details at: https://stackoverflow.com/a/50625086/3899136
    """
    if op in ("==", "!="):
        return ["{0} {1} {2}".format(left, op, right)]


def pytest_configure():
    settings.configure(
        INSTALLED_APPS=["django_stomp"],
        STOMP_SERVER_HOST=os.getenv("STOMP_SERVER_HOST"),
        STOMP_SERVER_PORT=os.getenv("STOMP_SERVER_PORT"),
        STOMP_SERVER_USER=os.getenv("STOMP_SERVER_USER"),
        STOMP_SERVER_PASSWORD=os.getenv("STOMP_SERVER_PASSWORD"),
        STOMP_USE_SSL=os.getenv("STOMP_USE_SSL"),
    )