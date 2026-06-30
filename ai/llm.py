# This file is what talks to the local LLM (or SLM because my little laptop isn't capable as the billion dollar datacenters polluting the world lol)
# Install ollama in your environment if you want local LLM support.
# idk how to do this part

# used the following command to install it. Kinda important and took me way too long to figure out:
# python -m pip install ollama
import ollama

def ask_llm(prompt):
    response = ollama.chat(
        model="",
        messages=[{"role": "user", "content":prompt}]
    )

    return response["message"]["content"]