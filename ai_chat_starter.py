import os
from openai import OpenAI

# Initialize Client (Get your key from platform.openai.com)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_ai(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    user_input = input("Enter your prompt for the AI: ")
    print(f"\nAI Response:\n{chat_with_ai(user_input)}")
