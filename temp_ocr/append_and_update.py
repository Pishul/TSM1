import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

target_file = sys.argv[1]
text_file = sys.argv[2]

with open(text_file, 'r', encoding='utf-8') as f:
    text = f.read()

with open(target_file, 'a', encoding='utf-8') as f:
    f.write("\n" + text + "\n")

state_file = r"a:\Downloads\TSM1-Final\TSM1\temp_ocr\ocr_state.json"
if os.path.exists(state_file):
    with open(state_file, 'r', encoding='utf-8') as f:
        state = json.load(f)
else:
    state = {"processed": 0}

state["processed"] += 1

with open(state_file, 'w', encoding='utf-8') as f:
    json.dump(state, f)

print(f"Appended to {target_file} and state processed: {state['processed']}")
