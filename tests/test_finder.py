from fuzzyget import finder
import pytest


def test_file_reading():
    assert finder.finder("nllsh", "poggy") == ("yo!",)


def test_file_doesnt_exit():
    assert finder.finder("twitchuser1234", "poggy") == ("User not found!",)
