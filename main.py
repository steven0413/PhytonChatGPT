import openai
import config

openai.api_key = config.api_key

response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "¿Cuál es la misión de OpenAI?"}], # Corrected 'messages' and 'user' role
)
print(response)
