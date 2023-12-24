from fuzzyget import finder
import pytest


def test_file_reading():
    assert finder.find("nllsh", "poggy") == ("yo!",)


def test_file_doesnt_exit():
    assert finder.find("twitchuser1234", "poggy") == ("User not found!",)
