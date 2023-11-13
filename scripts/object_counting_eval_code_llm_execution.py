import copy
import json
import argparse
import tqdm
import os
import traceback

from pal import interface
from pal.prompt import object_counting_prompt_code_llm_execution

parser = argparse.ArgumentParser()
parser.add_argument('--append', action='store_true')
parser.add_argument('--verbose', action='store_true')
parser.add_argument('--dataset', default='gsm', type=str)
parser.add_argument('--model', default='gpt-3.5-turbo', type=str)
parser.add_argument('--temperature', default=0.0, type=float)
parser.add_argument('--top_p', default=1.0, type=float)
parser.add_argument('--max_tokens', default=512, type=int)
parser.add_argument('--majority_at', default=None, type=int)
args = parser.parse_args()

DATA_PATH = f'datasets/{args.dataset}.jsonl'
OUTPUT_PATH = f'eval_results/{args.dataset}_chatgpt_llm_execution_k_{args.majority_at}.jsonl'
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

examples = list(map(json.loads, open(DATA_PATH)))

itf = interface.TextChatInterface(
    stop=None,
    model=args.model,
    verbose=args.verbose,
    system_message=object_counting_prompt_code_llm_execution.OBJECT_COUNTING_BETA_SYSTEM_MESSAGE,
    should_extract_answer=True
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
            ans = itf.run(
                object_counting_prompt_code_llm_execution.OBJECT_COUNTING_PROMPT.format(question=question),
                temperature=args.temperature,
                top_p=args.top_p,
                max_tokens=args.max_tokens,
                majority_at=args.majority_at
            )
            ans = float(ans)
            score = 1 if abs(ans - float(x['target'])) < 1e-3 else 0
        except Exception as e:
            traceback.print_exc()
            print(e)
            ans = ''
            score = 0
        scores.append(score)

        result['answer'] = ans
        result['score'] = score
        result['generation'] = itf.history
        result['candidate_answers'] = itf.results
        result['calibration_results'] = itf.calibration_results
        f.write(json.dumps(result) + '\n')

        itf.clear_history()
        itf.clear_results()
        itf.clear_calibration_results()
        f.flush()

print(f'Accuracy - {sum(scores) / len(scores)}')