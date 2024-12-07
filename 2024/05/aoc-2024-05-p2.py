# dunno why did it return the correct answer (4655) b/c the newly ordered "updates" are in reverse order...

import functools
import sys
from itertools import combinations

if len(sys.argv) < 2:
    print("Error: missing input file!")
    exit(1)

with open(sys.argv[1], "r") as f:
    content = f.read()

corrected_middles = 0
correct_updates = []
incorrect_updates = []
split_content = content.split("\n\n")
rules = split_content[0].splitlines()
updates = []
for sc in split_content[1].splitlines():
    updates.append(sc.split(","))


def elf_sort(a, b):
    current_rule = f"{a}|{b}"
    if current_rule in rules:
        return 0
    
    current_rule = f"{b}|{a}"
    if current_rule in rules:
        return -1

    return 0



def is_rule_violated_by_update(update):
    for c in combinations(update, 2):
        try:
            current_rule = f"{c[1]}|{c[0]}"
            rules.index(current_rule)
            # print(f"\033[91mrule [{current_rule}] violated in {update}\033[0m")
            return [c[0], c[1]]
        except ValueError:
            pass

    return None


fixed = 0
for update in updates:
    rule_violated = is_rule_violated_by_update(update)

    if rule_violated:
        is_corrected_ok = False

        while not is_corrected_ok:
            correct_update = sorted(update, key=functools.cmp_to_key(elf_sort))

            is_corrected_ok = is_rule_violated_by_update(correct_update)

        if not is_corrected_ok:
            # print(f"\033[91m{update}\n{correct_update} - {is_corrected_ok}\033[0m")
            exit(1)
        
        middle = eval(correct_update[(len(correct_update) // 2)])
        # print(f"\033[92m{update}\n{correct_update} - {is_corrected_ok} ; update looks good, its middle is {middle}\033[0m")

        corrected_middles += middle

        fixed += 1

print(f"Sum of the corrected middles is '{corrected_middles}' ('{fixed} fixed')")
