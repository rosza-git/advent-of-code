import sys
from itertools import combinations

if len(sys.argv) < 2:
    print("Error: missing input file!")
    exit(1)

with open(sys.argv[1], "r") as f:
    content = f.read()

middles = 0
correct_updates = []
incorrect_updates = []
violated_rules = []
split_content = content.split("\n\n")
rules = split_content[0].splitlines()
updates = []
for sc in split_content[1].splitlines():
    updates.append(sc.split(","))


for update in updates:
    rule_violated = False

    for c in combinations(update, 2):
        try:
            current_rule = f"{c[1]}|{c[0]}"
            rules.index(current_rule)
            rule_violated = True
            violated_rules.append(current_rule)
            print(f"\033[91mrule [{current_rule}] violated in {update}\033[0m")
            break
        except ValueError:
            pass

    if not rule_violated:
        middle = eval(update[(len(update) // 2)])
        correct_updates.append(update)
        # print(f"\033[92m{update} update looks good, its middle is {middle}\033[0m")

        middles += middle

    else:
        incorrect_updates.append(update)

print(f"Sum of the middles is '{middles}'")
print(f"Out of '{len(updates)}' updates '{len(correct_updates)}' are correct")
print(f"Out of '{len(updates)}' updates '{len(incorrect_updates)}' are incorrect")
print(f"Out of '{len(rules)}' rules are '{len(violated_rules)}' voilated")
