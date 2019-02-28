"""
https://github.com/huggingface/pytorch-pretrained-BERT#squad

Runs a squad eval
"""

import os

command = 'python ./BERT/examples/run_squad.py \
--bert_model bert-base-uncased \
--output_dir tmp \
--do_predict \
--predict_file ./squad-starter/data/dev-v2.0.json'

os.system(command)
