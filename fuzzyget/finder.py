from venv import logger
from logger import get_logger

from thefuzz import process as fuzz_process

LOGGER = get_logger()
MATCH_LIMIT = 3


def compare(lines: list[str], phrase: str) -> list[str]:
    global LOGGER

    matches = list()

    LOGGER.info(f"Attempting to find phrase {phrase}")
    results = fuzz_process.extract(phrase, lines, limit=MATCH_LIMIT)

    LOGGER.info(f"Top match: {results[0][0].strip()} with score {results[0][1]}")

    for match in results:
        matches.append(match[0].strip())

    return matches


def finder(user: str, phrase: str) -> list:
    global LOGGER
    try:
        with open(f"./userdata/{user}.txt") as f:
            contents: list[str] = f.readlines()
            LOGGER.info(f"File found: {user}.txt")
            matches = compare(contents, phrase)
            return matches

    except FileNotFoundError:
        LOGGER.error(f"File not found: {user}.txt")
        return list("User not found!")


print(finder("nllsh", "b"))
