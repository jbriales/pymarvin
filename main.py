#!/usr/bin/env python2
# coding=utf-8
"""Script to explore Marvin backup json"""

import json
import re

path_file = 'MarvinBackup-20181007.json'
with open(path_file, 'r') as f:
    d = json.load(f)

if False:
    print("Explore manually")
    str_note = d[66]['note']
    with open('temp', 'w') as f:
        f.write(str_note)
    dict_note = json.loads(str_note.lstrip('__S:'))

# Find string in all notes
r = re.compile("lingus", re.IGNORECASE)
for entry in d:
    if 'note' in entry and entry['note']:
        m = r.search(entry['note'])
        if m:
            print("Found keyword!")
            print("Title: {title}".format(**entry))
