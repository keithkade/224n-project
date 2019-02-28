"""
This parses the original training data and creates a new subset file, useful for
local development. After making the new file, you'll need to pass it to setup.py
as a command-line arg. ex: python setup.py --train_file='./data/train-v2.0-subset.json'
"""

import json
from pprint import pprint

subset = {}

with open('squad-starter/data/train-v2.0.json') as file:
    original = json.load(file)

    # Example of how to loop through the data
    # for article in original['data']:
    #     for paragraph in article['paragraphs']:
    #         for qas in paragraph['qas']:
    #             total += 1

    # For testing, just use the first questions
    subset['version'] = original['version']
    subset['data'] = []
    subset['data'].append(original['data'][0])

    with open('squad-starter/data/train-v2.0-subset.json', 'w') as outfile:
        json.dump(subset, outfile)
