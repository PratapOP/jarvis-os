from brain.llm import ask_llm

while True:
    q = input("You: ")
    print("Jarvis:", ask_llm(q))
