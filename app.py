import json
import openai

print('reading')
with open('config.json', 'r') as jsonfile:
    data = json.load(jsonfile)
    print('read Success')

print(data)

openai.api_key = data['API_KEY']

# assigning base role to the AI
messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant."},
]

def chatbot(input): 
    if input:
        messages.append({ 'role' : 'user', 'content' : input})
        chat = openai.ChatCompletion.create(
            model='gpt-3.5-turbo', messages=messages
        )

        reply = chat.choices[0].message.content
        messages.append({ 'role' : 'assistant', 'content' : reply })

        return reply


def chatbot_runner():
    while True:
        val = input('tell something (type bye to exit) \n')
        if val.lower() == 'bye':
            break
        else:
            rep = chatbot(val)
            print(rep)

chatbot_runner()

