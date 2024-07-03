import requests
import json
from datasets import load_dataset
from tqdm import tqdm

def make_openai_request(content: str, model: str = "string", temperature: float = 0, max_tokens: int = 0, url: str = "http://stargate:8000/v1/chat/completions"):
    payload = {
        "model": model,
        "messages": [
            { "role": "user", "content": content }
        ],
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    headers = { "Content-Type": "application/json" }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

def process_item(prompt: str):
    response = make_openai_request(prompt, max_tokens=2048)
    return {'prompt': prompt, 'response': response}

def process_dataset(dataset_name: str):
    dataset = load_dataset(dataset_name)
    train_data = dataset['test']
    results = []
    for item in tqdm(train_data, desc="Processing prompts"):
        result = process_item(item['prompt'])
        results.append(result)
    return results

def main():
    DATASET_NAME = "verifiers-for-code/humaneval_plan_generation"
    results = process_dataset(DATASET_NAME)
    print(f"Processed {len(results)} items")

if __name__ == "__main__":
    main()
