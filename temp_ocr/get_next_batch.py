import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

queue_file = r"a:\Downloads\TSM1-Final\TSM1\temp_ocr\ocr_queue.json"
state_file = r"a:\Downloads\TSM1-Final\TSM1\temp_ocr\ocr_state.json"

with open(queue_file, 'r', encoding='utf-8') as f:
    queue = json.load(f)

if os.path.exists(state_file):
    with open(state_file, 'r', encoding='utf-8') as f:
        state = json.load(f)
else:
    state = {"processed": 0}

processed = state["processed"]
batch_size = 5

next_batch = queue[processed:processed+batch_size]
print("BATCH_START")
for task in next_batch:
    print(json.dumps(task, ensure_ascii=False))
print("BATCH_END")
