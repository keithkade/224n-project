"""
This parses the original training data and creates a new subset file, useful for
local development. After making the new file, you'll need to pass it to setup.py
as a command-line arg. ex: python setup.py --train_file='./data/train-v2.0-subset.json'
"""

import json
import math
from pprint import pprint

subset = {}
data_size = 1000
count = 0

impossible_questions = math.ceil(data_size / 2)
impossible_questions_count = 0

questions_per_article = math.ceil(data_size / 442)

# there are 442 articles, with a number of paragraphs each
# for example, the Beyonce article has 66 paragraphs.
# then each of those are a number of questions (130319 total)

with open('squad-starter/data/train-v2.0.json') as file:
    original = json.load(file)

    # Example of how to loop through the data
    # for article in original['data']:
    #     for paragraph in article['paragraphs']:
    #         for qas in paragraph['qas']:
    #             count += 1

    # For testing, just use the first questions
    # subset['version'] = original['version']
    # subset['data'] = []
    # subset['data'].append(original['data'][0])

    # Smarter version - uses varied sampling of questions
    subset['version'] = original['version']

    subset['data'] = []
    total_questions_added = 0
    for article in original['data']:
        if total_questions_added >= data_size:
            break

        questions_added_for_article = 0
        new_article = {}
        new_article['title'] = article['title']
        new_article['paragraphs'] = []

        for paragraph in article['paragraphs']:
            if total_questions_added >= data_size:
                break
            if questions_added_for_article >= questions_per_article:
                break

            new_paragraph = {}
            new_paragraph['context'] = paragraph['context']

            # get a 50/50 impossibel question split
            if impossible_questions_count < impossible_questions:
                added_impossible = False
                for question in paragraph['qas']:
                    if question['is_impossible']:
                        new_paragraph['qas'] = [question]
                        impossible_questions_count += 1
                        added_impossible = True
                        break
                if not added_impossible:
                    new_paragraph['qas'] = [paragraph['qas'][0]]
            else:
                new_paragraph['qas'] = [paragraph['qas'][0]]

            new_article['paragraphs'].append(new_paragraph)

            total_questions_added += 1
            questions_added_for_article += 1

        subset['data'].append(new_article)

    for article in subset['data']:
        for paragraph in article['paragraphs']:
            for qas in paragraph['qas']:
                count += 1

    print(count)

    with open('squad-starter/data/train-v2.0-subset.json', 'w') as outfile:
        json.dump(subset, outfile)
