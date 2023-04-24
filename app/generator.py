import openai
from dotenv import my_key

openai.api_key = my_key

def generate_text(keyword):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Write a short story on the theme of '{keyword}'",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    if response.choices:
        generated_text = response.choices[0].text.strip()
        if keyword not in generated_text:
            generated_text = f"{keyword} {generated_text}"
        return generated_text
    else:
        return ""