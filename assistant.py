import openai

# Replace with your actual API key
openai.api_key = "your-api-key-here"

def get_ai_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    print("Simple AI Assistant")
    print("Type 'quit' to exit")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break

        ai_response = get_ai_response(user_input)
        print(f"AI: {ai_response}")

if __name__ == "__main__":
    main()