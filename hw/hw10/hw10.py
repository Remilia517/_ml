import ollama

def chat_with_model():
    model_name = 'llama3:latest'
    messages = []

    while True:
        user_input = input("👤 You: ")
        if user_input.lower() in ['exit', 'quit']:
            break

        messages.append({'role': 'user', 'content': user_input})

        response = ollama.chat(model=model_name, messages=messages)
        reply = response['message']['content']
        print("🤖 AI:", reply)

        messages.append({'role': 'assistant', 'content': reply})

if __name__ == "__main__":
    chat_with_model()
