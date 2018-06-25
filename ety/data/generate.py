"""
This script downloads source data from data.jmsv.me; this contains an unzipped
and filtered mirror of the http://www1.icsi.berkeley.edu/~demelo/etymwn dataset

Data was filtered using the script at: https://data.jmsv.me/etymwn-filterer.sh
"""

import csv
import hashlib
import os
import io
import json
import gc

import requests
import six
from clint.textui import progress


def prepare(source_dir):
    """
    Create data source directory if not exists
    """
    if not os.path.exists(source_dir):
        os.makedirs(source_dir)


def download_dataset(url, dl_path):
    """
    Download filtered etymwn from jmsv.me mirror, displaying progress bar
    """
    r = requests.get(url, stream=True)

    with open(dl_path, 'wb') as f:
        total_length = int(r.headers.get('content-length'))
        chunk_size = 4096
        for chunk in progress.bar(
                r.iter_content(chunk_size=chunk_size),
                expected_size=(total_length / chunk_size) + 1):
            if chunk:
                f.write(chunk)
                f.flush()
    print('Downloaded to ' + dl_path)


def verify_local_data(url, dl_path):
    """
    Compare actual file checksum with expected served checksum
    Return bool determines whether or not data is (re)downloaded
    :return: True if local file matches, otherwise False
    """
    try:
        with open(dl_path, 'rb') as f:
            # Local file checksum
            actual = hashlib.md5(f.read()).hexdigest()
    except EnvironmentError:
        # Return False if file doesn't exit
        return False

    expected = requests.get('%s.checksum' % url).text.strip()
    return actual == expected


def split_elements(compound):
    """
    Split source tsv elements at colon
    e.g.: 'rel:etymology' => ['rel', 'etymology']
    :return: Elements as list
    """
    elements = [e.strip() for e in compound.split(':')]
    if len(elements) == 2:
        return elements

    result = [elements[0], ':'.join(elements[1:])]
    return result


def generate_json(source_path, dir):
    """
    Reads source tsv and restructures data as described:
    https://github.com/jmsv/ety-python/issues/24
    """
    result = {}

    print('Loading source tsv')
    with io.open(source_path, 'r', newline='', encoding='utf-8') as source:
        reader = csv.reader(source, delimiter='\t')
        source_rows = list(reader)

    gc.collect()

    print('Structuring data')
    for row in progress.bar(source_rows):
        source_lang, source_word = split_elements(row[0])

        if source_lang not in result:
            result[source_lang] = {}
        if source_word not in result[source_lang]:
            result[source_lang][source_word] = []

        dest_lang, dest_word = split_elements(row[2])
        result[source_lang][source_word].append({dest_word: dest_lang})

        del source_lang, source_word, dest_lang, dest_word

    # Save data to seperate files for languages, may be required in the future
    # print('Saving language files')
    # for key in progress.bar(result):
    #     with io.open(os.path.join(dir, 'data/ety-%s.json' % key), 'w') as f:
    #         f.write(json.dumps(result[key], sort_keys=False))

    # Save data
    print('Writing etymologies file')
    with io.open(os.path.join(dir, 'etymologies.json'), 'w') as f:
        json.dump(result, f)


def main():
    """
    Define paths, download data if required, generate json dataset
    """
    dir = os.path.dirname(os.path.realpath(__file__))
    source_dir = os.path.join(dir, 'source')
    source_path = os.path.join(source_dir, 'etymwn.tsv')
    source_url = 'https://data.jmsv.me/etymwn-filtered.tsv'

    # Exit if not Python 3
    if not six.PY3:
        print("Script should be run as Python 3, exiting")
        exit(1)

    prepare(source_dir)

    # (Re)download data if required
    if not verify_local_data(source_url, source_path):
        print('Downloading source data')
        download_dataset(source_url, source_path)

        # If checksum still doesn't match, exit
        if verify_local_data(source_url, source_path):
            print('Verified local source data')
        else:
            print('Error verifying local source data, exiting')
            exit(1)
    else:
        print('Verified local source data')

    generate_json(source_path, dir)

    print('Done')


if __name__ == '__main__':
    main()
