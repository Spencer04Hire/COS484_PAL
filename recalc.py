import json
import re
import os

num  = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", 
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}


def strip_non_digit_edges(s):
    # Match from the first digit to the last digit (inclusive)
    match = re.search(r'-?\d(?:.*\d)?', s)
    return match.group(0) if match else ''

def recalc(path, debug=False, diff=False):
    results = list(map(json.loads, open(path)))
    total = 0
    for result in results:
        target = result["target"]
        numeric = True
        try:
            parsed_target = float(target)
        except:
            numeric = False

        parsed = result["answer"]
        if parsed[:2] == "A:":
            parsed = parsed[2:].strip()

        score = 0

        if numeric:
            parsed = num.get(parsed, parsed)
            answer = strip_non_digit_edges(parsed).replace(',', '')
            try:
                parsed_ans = float(answer)
                p = 5e-3
                if abs(parsed_target) < 1 and abs(parsed_target) != 0:
                    p = 0.005*abs(parsed_target)
                score = 1 if abs(parsed_ans - parsed_target) < p else 0
            except:
                score = 0
        else:
            answer = parsed.strip()
            score = 1 if answer.lower() == str(target).lower() else 0
            if target.lower() == "yes" and answer.lower() == "true":
                score = 1
            if target.lower() == "no" and answer.lower() == "false":
                score = 1

        if score == 1:
            total += 1
            if diff and result["score"] == 0:
                print(f"Now correct: {target}, {answer}, {result['answer']}")
        else:
            if debug:
                print(f"{target}, {answer}, {result['answer']}")
            if diff and result["score"] == 1:
                print(f"Now incorrect: {target}, {answer}, {result['answer']}")
    return total/len(results)

def results(lang, start=1, end=3, diff=False):
    print(lang)
    files = sorted(os.listdir(f'pal/eval_results1/{lang}/'))
    for f in files:
        for i in range(start,end+1):
            path = f"pal/eval_results{i}/{lang}/{f}"
            acc = recalc(path, diff=diff)
            print(f"{f[:-6]} Run {i}: {acc}")

lang = "Java"
start = 1
end = 1
# results(lang, start, end, True)

# ['date_understanding', 'gsm', 'gsmhardv2', 'mawpsaddsub', 'mawpsmultiarith', 'mawpssingleeq', 'mawpssingleop', 'object_counting', 'penguins_in_a_table', 'reasoning_about_colored_objects', 'repeat_copy', 'svamp']
languages = ['COT','Cpp','Direct','Java','Ocaml','Python']
start = 1
end = 5
for i in range(start, end+1):
    for lang in languages:
        path = f'pal/eval_results{i}/{lang}/reasoning_about_colored_objects.jsonl'
        print(f'{lang} Run {i}: {recalc(path, debug=False, diff=False)}')