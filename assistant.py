from transformers import GPTJForCausalLM, AutoTokenizer
import torch

def load_model_and_tokenizer():
    print("Loading model and tokenizer... This may take a few minutes.")
    model = GPTJForCausalLM.from_pretrained("EleutherAI/gpt-j-6B", torch_dtype=torch.float16, low_cpu_mem_usage=True)
    tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")
    return model, tokenizer

def get_ai_response(prompt, model, tokenizer):
    try:
        input_ids = tokenizer.encode(prompt, return_tensors="pt")
        output = model.generate(input_ids, max_length=100, num_return_sequences=1)
        response = tokenizer.decode(output[0], skip_special_tokens=True)
        return response[len(prompt):].strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    print("Simple AI Assistant using GPT-J")
    print("Loading model... This may take a few minutes.")
    model, tokenizer = load_model_and_tokenizer()
    print("Model loaded. Type 'quit' to exit")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break

        ai_response = get_ai_response(user_input, model, tokenizer)
        print(f"AI: {ai_response}")

if __name__ == "__main__":
    main()