import openai
import time

openai.api_key = 'your-openai-api-key'

class Assistant:
    def __init__(self, name):
        self.name = name
        self.conversation_history = []

    def add_message(self, role, content):
        self.conversation_history.append({"role": role, "content": content})

    def generate_message(self, prompt):
        self.add_message("user", prompt)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.conversation_history
        )
        message = response['choices'][0]['message']['content']
        self.add_message("assistant", message)
        return message

assistant1 = Assistant("Assistant 1")
assistant2 = Assistant("Assistant 2")

# Initialize the conversation
assistant1.add_message("system", "You are a helpful assistant.")
assistant2.add_message("system", "You are a helpful assistant.")

# Start the conversation with a question
question = "Tell me an interesting fact about the universe."
print(f"{assistant1.name}: {question}")
response = assistant2.generate_message(question)

# Now let the assistants talk to each other
for i in range(10):
    print(f"{assistant2.name}: {response}")
    time.sleep(1) # optional delay for readability
    response = assistant1.generate_message(response)
    print(f"{assistant1.name}: {response}")
    time.sleep(1) # optional delay for readability
    response = assistant2.generate_message(response)
