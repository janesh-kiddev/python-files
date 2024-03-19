import openai

openai.api_key = "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"


def chat_bot(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{'role': 'user', "content": prompt}]
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    while True:
        user = input("YOU:")
        if user.lower() in ['exit', 'quit', 'bye']:
            break

        response = chat_bot(user)
        print('Chatbot:', response)
