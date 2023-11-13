# Copyright 2022 PAL Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import copy
import json
import argparse
import tqdm
import datetime
from pal import interface, runtime
from pal.prompt import date_understanding_prompt

parser = argparse.ArgumentParser()
parser.add_argument('--append', action='store_true')
parser.add_argument('--verbose', action='store_true')
parser.add_argument('--dataset', default='gsm', type=str)
parser.add_argument('--model', default='code-davinci-002', type=str)
parser.add_argument('--majority_at', default=None, type=int)
parser.add_argument('--temperature', default=0.0, type=float)
parser.add_argument('--top_p', default=1.0, type=float)
parser.add_argument('--max_tokens', default=256, type=int)
args = parser.parse_args()

DATA_PATH = 'datasets/date_understanding.json'
OUTPUT_PATH = f'eval_results/{args.dataset}_code_{args.model}_t_{args.temperature}_k_{args.majority_at}.jsonl'

examples = json.load(open(DATA_PATH))['examples']

itf = interface.ProgramInterface(
    runtime=runtime.DateRuntime(),
    stop='\n\n',
    verbose=args.verbose
)

if args.append:
    lines = open(OUTPUT_PATH).readlines()
    num_skip_exps = len(lines)
    scores = [x['score'] for x in map(json.loads, lines)]
else:
    num_skip_exps = 0
    scores = []

with open(OUTPUT_PATH, 'a' if args.append else 'w') as f:
    pbar = tqdm.tqdm(examples[num_skip_exps:], initial=num_skip_exps, total=len(examples))
    for x in pbar:
        question = x['input']
        result = copy.copy(x)
        try:
            ans_str = itf.run(date_understanding_prompt.DATE_UNDERSTANDING_PROMPT.format(
				question=question), majority_at=args.majority_at,
				temperature=args.temperature, top_p=args.top_p,
				max_tokens=args.max_tokens)
            if isinstance(ans_str, datetime.datetime):
                ans_str = ans_str.strftime('%m/%d/%Y')
            result['answer'] = ans_str
            score = x['target_scores'][ans_str]
        except:
            score = 0
        scores.append(score)

        for i in range(len(itf.results)):
            try:
                if isinstance(itf.results[i], datetime.datetime):
                    itf.results[i] = itf.results[i].strftime('%m/%d/%Y')
            except:
                itf.results[i] = ''
                                
        # result['answer'] = ans
        result['score'] = score
        result['generation'] = itf.history
        result['candidate_answers'] = itf.results
        result['calibration_results'] = itf.calibration_results
        try:
            f.write(json.dumps(result) + '\n')
        except:
            print("Result error")
            print(result)
            f.write('\n')

        itf.clear_history()
        itf.clear_results()
        itf.clear_calibration_results()
        f.flush()

print(f'Accuracy - {sum(scores) / len(scores)}')