# ibus-replace-with-kanji - Replace with Kanji Japanese input method for IBus
#
# Copyright (c) 2017-2020 Esrille Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import locale
import os

_uitexts = {}


def _(string):
    global _uitexts
    if string in _uitexts:
        return _uitexts[string]
    return string


def initialize():
    global _uitexts
    lang = locale.getdefaultlocale()[0]
    filename = os.path.join(os.getenv("IBUS_REPLACE_WITH_KANJI_LOCATION"), "locale")
    filename = os.path.join(filename, "ibus-replace-with-kanji." + lang + ".json")
    try:
        with open(filename, 'r') as file:
            _uitexts = json.load(file)
    except:
        pass
