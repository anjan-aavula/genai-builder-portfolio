import os
from dotenv import load_dotenv
from openai import OpenAI
from rich import print

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# 🧠 Prompt templates (this is the "GenAI skill layer")
def build_prompt(mode, user_input):
    prompts = {
        "chat": user_input,

        "summarize": f"""
Summarize the following text in simple bullet points:

Text:
{user_input}
""",

        "explain": f"""
Explain this like I'm a beginner (simple language, real-world examples):

Topic:
{user_input}
""",

        "rewrite": f"""
Rewrite this text in a professional tone:

Text:
{user_input}
""",

        "creative": f"""
Turn this into a creative story or idea:

Input:
{user_input}
"""
    }

    return prompts.get(mode, user_input)


def ask_ai(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a smart, helpful AI assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


def show_menu():
    print("\n[bold cyan]=== Prompt Playground Modes ===[/bold cyan]")
    print("[1] Chat Mode")
    print("[2] Summarize Text")
    print("[3] Explain Topic")
    print("[4] Rewrite Text")
    print("[5] Creative Mode")
    print("[6] Exit")


def get_mode(choice):
    return {
        "1": "chat",
        "2": "summarize",
        "3": "explain",
        "4": "rewrite",
        "5": "creative"
    }.get(choice, "chat")


print("[bold green]🔥 Welcome to GenAI Prompt Playground[/bold green]")

while True:
    show_menu()

    choice = input("\nSelect mode (1-6): ")

    if choice == "6":
        print("[red]Goodbye 👋[/red]")
        break

    mode = get_mode(choice)

    user_input = input("\nEnter your input: ")

    prompt = build_prompt(mode, user_input)

    print("\n[yellow]Thinking... 🤖[/yellow]\n")

    result = ask_ai(prompt)

    print("\n[bold magenta]AI Response:[/bold magenta]\n")
    print(result)
    print("\n" + "-" * 50 + "\n")