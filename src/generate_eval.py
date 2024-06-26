import os
import subprocess
from vllm import LLM, SamplingParams
from datasets import load_dataset
from transformers import AutoTokenizer
from evalplus.data import get_human_eval_plus
import json

# ==== CONFIG ==== #
# Model
MODEL = "microsoft/Phi-3-mini-4k-instruct"
MODEL_NAME = MODEL.split('/')[-1]
# HF
DATASET = "verifiers-for-code/humaneval_plan_generation"
# Output dir name
OUTPUT_DIR = MODEL_NAME + "-output"
# Choose GPU Count
NUM_GPUS = 1
# Choose what GPUs to use
os.environ["CUDA_VISIBLE_DEVICES"] = "3"
# Evaluation flags, True if you want to evaluate
EVAL_GOLD = True
GOLD_PROMPT_COL = "cleaned_sonnet-3.5_gold_plans"
EVAL_NONE = True
NONE_PROMPT_COL = "prompt"
# New Token Count
MAX_TOKENS = 2048
# ==== END CONFIG ==== #
__MAGIC_SPLITTER__ = "-[[]]-this-is-really-our-highest-priority-[[]]-"

def main():
    response = f"""
Below is a self-contained Python script that solves the problem: 
```python 
{__MAGIC_SPLITTER__}
```
"""

    llm = LLM(model=MODEL, 
              tensor_parallel_size=NUM_GPUS, 
              enable_prefix_caching=False, 
              gpu_memory_utilization=0.95, 
              max_model_len=2048, 
              trust_remote_code=True,
              max_num_seqs=16)

    tokenizer = llm.get_tokenizer()

    sampling_params = SamplingParams(
        temperature=0, top_p=0.95, max_tokens=MAX_TOKENS,
    )

    if EVAL_GOLD:
        process_mode("gold_plan", DATASET, GOLD_PROMPT_COL, llm, tokenizer, sampling_params, response)

    if EVAL_NONE:
        process_mode("none", DATASET, NONE_PROMPT_COL, llm, tokenizer, sampling_params, response)

def process_mode(mode, dataset_name, prompt_key, llm, tokenizer, sampling_params, response):
    dataset = load_dataset(dataset_name, split="test")
    
    prompts = [create_prompts(task[prompt_key], tokenizer, response, __MAGIC_SPLITTER__) for task in dataset]

    print(f"Sample prompt for {mode}:")
    print(prompts[0])

    generated_solutions = get_vllm_code(llm, prompts, sampling_params)

    # Uncomment the following lines if you want to update the dataset
    # dataset = update_dataset_with_solutions(dataset, COLUMN_NAME, generated_solutions)
    # dataset.push_to_hub(dataset_name)

    clean_solutions = [extract_clean_code(code) for code in generated_solutions]

    output_dir = os.path.join(OUTPUT_DIR, mode)
    for index, solution in enumerate(clean_solutions):
        name = f"HumanEval_{index}"
        os.makedirs(os.path.join(output_dir, name), exist_ok=True)
        with open(os.path.join(output_dir, name, '0.py'), 'w', encoding='utf-8') as f:
            f.write(solution)

    convert_to_jsonl(clean_solutions, os.path.join(output_dir, 'solutions.jsonl'))

    print(f"Generation completed for {mode}")
    print(f"Output directory: {output_dir}")
    print(f"Running evaluation for {mode}")
    run_evalplus(output_dir)

def create_prompts(prompt, tokenizer, response, __MAGIC_SPLITTER__):
    prompt = f"Please provide a self-contained Python script that solves the following problem in a markdown code block. Follow the given plan.\n```\n{prompt.strip()}\n```\n"
    x = tokenizer.apply_chat_template(
        [
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": response},
        ],
        tokenize=False).split(__MAGIC_SPLITTER__)[0]
    return x

def get_vllm_code(llm, prompts, sampling_params):
    outputs = llm.generate(prompts, sampling_params)
    return [x.outputs[0].text for x in outputs]

def update_dataset_with_solutions(dataset, new_column_name, solutions):
    if new_column_name in dataset.column_names:
        dataset = dataset.remove_columns(new_column_name)
    return dataset.add_column(new_column_name, solutions)

def extract_clean_code(text):
    index = text.find("```")
    if index != -1:
        text = text[:index]
    lines = text.splitlines()
    for i, line in enumerate(reversed(lines)):
        if "return" in line:
            last_return_index = len(lines) - i - 1
            return '\n'.join(lines[:last_return_index+1])
    return text

def convert_to_jsonl(solutions, output_file):
    with open(output_file, 'w') as f:
        for i, solution in enumerate(solutions):
            json_line = json.dumps({"task_id": f"HumanEval/{i}", "completion": solution})
            f.write(json_line + '\n')

def run_evalplus(output_dir):
    command = f"evalplus.evaluate --dataset humaneval --samples {output_dir} --i-just-wanna-run"
    print(f"Running evaluation command: {command}")
    subprocess.run(command, shell=True, check=True)

if __name__ == "__main__":
    main()