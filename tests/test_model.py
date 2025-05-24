import warnings
warnings.simplefilter("ignore", DeprecationWarning)

import os
import sys
from pathlib import Path
import asyncio

from openai import OpenAI

root = str(Path(__file__).resolve().parents[1])
sys.path.append(root)

def test_deepseek():
    # Please install OpenAI SDK first: `pip3 install openai`

    from openai import OpenAI

    client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": "Hello"},
        ],
        stream=False
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":

    # model_name = "gpt-4o"
    # client = OpenAI(
    #     api_key=os.getenv("OPENAI_API_KEY"),
    #     base_url=os.getenv("OPENAI_BASE_URL"),
    # )
    
    # model_name = "deepseek-chat"
    model_name = "deepseek-reasoner"
    client = OpenAI(
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        base_url=os.getenv("DEEPSEEK_API_BASE"),
    )
    
    response = client.chat.completions.create(
        model=model_name, 
        messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Hello"}], 
        # stream=False,
        temperature=0,
        )
    print(response.choices[0].message.content)

