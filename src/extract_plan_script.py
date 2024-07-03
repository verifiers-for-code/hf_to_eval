import re
from datasets import load_dataset

# === CONFIGURATION === #
DATASET_NAME = "verifiers-for-code/humaneval_plan_generation"
COL_TO_CLEAN = "phi3-planner-plans"
COL_CLEANED_NAME = "cleaned-" + COL_TO_CLEAN
# === END CONFIGURATION === #

dataset = load_dataset(DATASET_NAME, split="test")

def extract_plan(text):
    match = re.search(r'<plan>(.*?)</plan>', text, re.DOTALL)
    if match:
        plan = match.group(1).strip()
        return plan.split('\n')
    return []

def insert_plan_into_docstring(prompt, plan):
    # Find the end of the docstring
    docstring_start = prompt.find('"""')
    docstring_end = prompt.find('"""', docstring_start + 3)
    
    # If there's no docstring or it's malformed, return the original prompt
    if docstring_end == -1:
        return prompt
    
    # Get the indentation of the closing docstring
    closing_indent = prompt.rfind('\n', 0, docstring_end) + 1
    indent = prompt[closing_indent:docstring_end].replace('"""', '')
    
    # Prepare the plan text with proper indentation
    plan_text = "\n\n" + indent + "Plan:\n" + "\n".join(indent + "    " + line for line in plan)
    
    return prompt[:docstring_end] + plan_text + prompt[docstring_end:]

# Apply the extraction and insertion to the dataset
def process_item(item):
    plan = extract_plan(item[COL_TO_CLEAN])
    new_prompt = insert_plan_into_docstring(item['prompt'], plan)
    return {COL_CLEANED_NAME: new_prompt}

dataset = dataset.map(process_item)

# Print a sample to verify
print(dataset[0][COL_CLEANED_NAME])

dataset.push_to_hub(DATASET_NAME, split="test")