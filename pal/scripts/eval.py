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
import os
import traceback

from pal import interface
from pal.prompt import math_prompt, penguin_prompt, date_understanding_prompt, algorithmic_prompt, colored_object_prompt
from pal.core.runtime import RUNTIME_DICT

DATASET_TO_PROMPT = {
    "object_counting": algorithmic_prompt.OBJECT_COUNTING_PROMPTS,
    "penguins_in_a_table": penguin_prompt.PENGUIN_PROMPTS,
    "repeat_copy": algorithmic_prompt.REPEAT_COPY_PROMPTS,
    "date_understanding": date_understanding_prompt.DATE_UNDERSTANDING_PROMPTS,
    "reasoning_about_colored_objects": colored_object_prompt.COLOR_OBJECT_PROMPTS,
    "gsm": math_prompt.MATH_PROMPTS,
    "gsmhardv2": math_prompt.MATH_PROMPTS,
    "svamp": math_prompt.MATH_PROMPTS,
    "mawpssingleeq": math_prompt.MATH_PROMPTS,
    "mawpssingleop": math_prompt.MATH_PROMPTS,
    "mawpsaddsub": math_prompt.MATH_PROMPTS,
    "mawpsmultiarith": math_prompt.MATH_PROMPTS
}

def get_jsonl_examples(data_path):
    return list(map(json.loads, open(data_path)))

def get_json_examples(data_path):
    examples = []
    file_obj = json.load(open(data_path))
    json_examples = file_obj["examples"]
    task_prefix = file_obj.get("task_prefix", "")
    
    for ex in json_examples:
        if "target" in ex:
            target = ex["target"]
        else:
            target = max(ex["target_scores"], key=ex["target_scores"].get)
        
        examples.append({
            "input": task_prefix + ex["input"],
            "target": target
        })
    return examples


DATASET_TO_EXAMPLES = {
    "object_counting": get_json_examples, 
    "penguins_in_a_table": get_json_examples,
    "repeat_copy": get_json_examples,
    "date_understanding": get_json_examples,
    "reasoning_about_colored_objects": get_json_examples,
    "gsm": get_jsonl_examples,
    "gsmhardv2": get_jsonl_examples,
    "svamp": get_jsonl_examples,
    "mawpssingleeq": get_jsonl_examples,
    "mawpssingleop": get_jsonl_examples,
    "mawpsaddsub": get_jsonl_examples,
    "mawpsmultiarith": get_jsonl_examples
}

LANGUAGE_TO_PROMPT = {
    "Direct": "You are a helpful assistant that can solve questions in a manner identical to the examples that you will be provided.",
    "COT": "You are a helpful assistant that can solve questions in a manner identical to the examples that you will be provided.",
    "Python": "You are a helpful expert Python programmer that can only write Python code that solves questions in a manner identical to the examples that you will be provided. In your code, please print the final result to standard out on a single line.",
    "Java": "You are a helpful expert Java programmer that can only write Java code that solves questions in a manner identical to the examples that you will be provided. Name your class as 'Solution'. In your code, please print the final result to standard out on a single line.",
    "Cpp": "You are a helpful expert C++ programmer that can only write C++ code that solves questions in a manner identical to the examples that you will be provided. In your code, please print the final result to standard out on a single line.",
    "Ocaml": "You are a helpful expert OCaml programmer that can only write OCaml code that solves questions in a manner identical to the examples that you will be provided. In your code, please print the final result to standard out on a single line.",
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', action='store_true')
    parser.add_argument('--dataset', required=True, type=str)
    parser.add_argument('--model', default='gpt-4o-mini', type=str)
    parser.add_argument('--temperature', default=0.0, type=float)
    parser.add_argument('--top_p', default=1.0, type=float)
    parser.add_argument('--max_tokens', default=1024, type=int)
    parser.add_argument('--language', default = "Python", type=str)
    parser.add_argument('--start_samples', default = 0, type = int)
    parser.add_argument('--end_samples', default = -1, type = int)

    args = parser.parse_args()
    language = args.language
    dataset = args.dataset
    start_samples = args.start_samples

    DATA_PATH = f'datasets/{dataset}.jsonl'
    OUTPUT_PATH = f"eval_results/{language}/{dataset}.jsonl"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    # List of python objects with input and target
    examples = DATASET_TO_EXAMPLES[args.dataset](DATA_PATH)

    end_samples = len(examples) - 1 if args.end_samples == -1 else args.end_samples

    itf = interface.ProgramChatInterface(
        stop='\n\n\n',
        get_answer_from_stdout=True,
        runtime=RUNTIME_DICT[language](),
        model=args.model,
        verbose=args.verbose,
        system_message=LANGUAGE_TO_PROMPT[language]
    )

    scores = []

    with open(OUTPUT_PATH, 'w') as f:
        pbar = tqdm.tqdm(examples[start_samples:end_samples + 1])
        for x in pbar:
            question = x['input']
            result = copy.copy(x)
            
            try:
                prompt = DATASET_TO_PROMPT[dataset][language] % (question)
                
                # print("Prompt: ")
                # print(prompt)
                ans = itf.run(prompt,
                              temperature=args.temperature, top_p=args.top_p,
                              max_tokens=args.max_tokens)

                try:
                    parsed_ans = float(ans)
                    parsed_target = float(x['target'])
                    score = 1 if abs(parsed_ans - parsed_target) < 1e-3 else 0
                except ValueError:
                    score = 1 if ans.lower() == str(x['target']).lower() else 0
                
            except Exception:
                print(traceback.format_exc())
                ans = ''
                score = 0
            scores.append(score)
            
            result['answer'] = ans
            result['score'] = score
            result['generation'] = itf.history
            f.write(json.dumps(result) + '\n')
            
            itf.clear_history()
            f.flush()

    print(f'Accuracy - {sum(scores) / len(scores)}')


if __name__ == '__main__':
    main()
