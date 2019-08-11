#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import io
import json

from pkg_resources import resource_filename


def load_json_resource(resource):
    resource = resource_filename("ety", resource)
    with io.open(resource, "r", encoding="utf-8") as f:
        return json.load(f)


def load_country_codes(iso_version):
    return load_json_resource("data/iso-{}.json".format(iso_version))


etyms = load_json_resource("data/etymologies.json")
iso_639_3_codes = load_country_codes("639-3")
iso_639_2_codes = load_country_codes("639-2")
