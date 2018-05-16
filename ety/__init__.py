import sys
from pkg_resources import resource_filename
import json
import random

with open(resource_filename('ety', 'origins.json'), 'r') as f:
    origins_dict = json.load(f)


def cli():
    if len(sys.argv) <= 1:
        print("No word supplied\n")
        print("Usage:\n  $ ety <word>\n")
        print("Example:\n  $ ety potato\n  Spanish, Taino")
        return

    word = sys.argv[1]

    try:
        origin = ', '.join(origins(word))
        print(origin)
    except ValueError as e:
        print(str(e))
    except Exception as e:
        print(e)


def origins(word):
    try:
        origin = origins_dict[word]
    except KeyError:
        error = "No etymology data available for word: %s" % word
        raise ValueError(error)

    return origin


def words(origin):
    result = []
    for word in origins_dict.keys():
        if origin.lower() in [o.lower() for o in origins_dict[word]]:
            result.append(word)
    return result


def random_word():
    return random.choice(list(origins_dict.keys()))
