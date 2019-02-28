import json
import csv

from pprint import pprint

with open('tmp/predictions.json') as file:
    json_preds = json.load(file)

    pred_arr = []

    for key in json_preds:
        pred_arr.append((key, json_preds[key]))

    with open('tmp/predictions.csv', 'w') as csv_fh:
        csv_writer = csv.writer(csv_fh, delimiter=',')

        csv_writer.writerow(['Id', 'Predicted'])

        for tuple in sorted(pred_arr):
            print([tuple[0], tuple[1]])
            csv_writer.writerow([tuple[0], tuple[1]])
