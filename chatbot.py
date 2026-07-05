import random
import time

# SECTION 1 — RESPONSE DATA
# All bot replies live here. Adding a new topic = adding one entry.


RESPONSES = {
    # ── Greetings ─────────────────────────────────────────────────
    "hello":          ["Hello! How can I help you today?",
                       "Hey there! What's on your mind?",
                       "Hi! Nice to see you."],

    "hi":             ["Hi! What can I do for you?",
                       "Hello! Go ahead, ask me anything."],

    "hey":            ["Hey! What's up?",
                       "Hey! How can I assist you?"],

    "good morning":   ["Good morning! Hope you have a great day ahead.",
                       "Morning! Ready to chat?"],

    "good night":     ["Good night! Sleep well.",
                       "Good night! Take care."],

    # ── Well-being ────────────────────────────────────────────────
    "how are you":    ["I'm doing great, thanks for asking!",
                       "Feeling fantastic! How about you?",
                       "All systems running perfectly!"],

    "what's up":      ["Not much — just here to chat!",
                       "All good on my end. What can I help with?"],

    # ── Identity ──────────────────────────────────────────────────
    "your name":      ["I'm Zeno, your friendly chatbot!",
                       "You can call me Zeno."],

    "who are you":    ["I'm Zeno — a simple rule-based chatbot "
                       "built with Python."],

    "what can you do":["I can chat with you, answer basic questions, "
                       "tell a joke, and share the current time!\n"
                       "Try typing 'help' to see all commands."],

    # ── Help ──────────────────────────────────────────────────────
    "help":           ["Here's what I understand:\n"
                       "  hello / hi / hey      — greetings\n"
                       "  how are you           — check on me\n"
                       "  who are you           — learn about me\n"
                       "  what can you do       — my capabilities\n"
                       "  tell me a joke        — I'll make you smile\n"
                       "  what time is it       — current time\n"
                       "  thank you             — you're welcome!\n"
                       "  bye / exit / quit     — end the chat"],

    # ── Jokes ─────────────────────────────────────────────────────
    "joke":           ["Why do programmers prefer dark mode?\n"
                       "  → Because light attracts bugs!",

                       "Why did the developer go broke?\n"
                       "  → Because he used up all his cache!",

                       "How many programmers does it take to change a bulb?\n"
                       "  → None — that's a hardware problem!",

                       "Why do Python programmers wear glasses?\n"
                       "  → Because they can't C!"],

    # ── Time ──────────────────────────────────────────────────────
    "time":           ["__CURRENT_TIME__"],   # resolved at runtime

    # ── Thanks ────────────────────────────────────────────────────
    "thank":          ["You're welcome!",
                       "Happy to help! Let me know if you need anything else.",
                       "Anytime!"],

    # ── Farewell ──────────────────────────────────────────────────
    "bye":            ["Goodbye! Have a wonderful day!",
                       "See you later! Take care."],

    "exit":           ["Exiting the chat. Goodbye!"],

    "quit":           ["Quitting now. It was nice chatting with you!"],
}

# Words that should end the session
EXIT_WORDS = {"bye", "exit", "quit"}

# Fallback replies when no keyword matches
FALLBACK_REPLIES = [
    "I didn't quite understand that. Try typing 'help'.",
    "Hmm, I'm not sure how to respond. Type 'help' for options.",
    "I'm still learning! Type 'help' to see what I understand.",
]


# SECTION 2 — CORE FUNCTIONS

def get_response(user_input):
    """
    Check user_input for known keywords and return a matching reply.
    Falls back to a default reply if nothing matches.

    Parameters:
        user_input (str): Raw text entered by the user.

    Returns:
        str: The chatbot's reply.
    """
    text = user_input.lower().strip()

    # Scan each keyword in the response dictionary
    for keyword, replies in RESPONSES.items():
        if keyword in text:
            reply = random.choice(replies)

            # Special case: resolve the time placeholder
            if reply == "__CURRENT_TIME__":
                reply = "The current time is " + time.strftime("%I:%M %p") + "."

            return reply

    # No keyword matched — return a fallback
    return random.choice(FALLBACK_REPLIES)


def is_exit_command(user_input):
    """
    Return True if the user wants to end the session.

    Parameters:
        user_input (str): Raw text entered by the user.

    Returns:
        bool
    """
    words = user_input.lower().strip().split()
    return bool(set(words) & EXIT_WORDS)


def display_banner():
    """Print the welcome banner when the chatbot starts."""
    border = "=" * 44
    print(border)
    print("           ZENO  —  Basic Chatbot")
    print("      Rule-Based Python Conversational AI")
    print(border)
    print("  Type 'help' for commands  |  'bye' to exit")
    print(border)


def display_separator():
    """Print a thin divider between turns."""
    print("-" * 44)


# SECTION 3 — MAIN CHAT LOOP

def run_chatbot():
    """
    Drive the conversation using a while loop.
    Keeps running until the user types an exit command.
    """
    display_banner()

    while True:
        try:
            # --- Input ---
            user_input = input("\nYou   : ").strip()

            # Ignore blank lines
            if not user_input:
                print("Zeno  : Please type something. (Hint: try 'help')")
                display_separator()
                continue

            # --- Process & Respond ---
            response = get_response(user_input)
            print(f"Zeno  : {response}")
            display_separator()

            # --- Check Exit ---
            if is_exit_command(user_input):
                break

        except KeyboardInterrupt:
            # Handle Ctrl+C cleanly without a traceback
            print("\nZeno  : Session interrupted. Goodbye!")
            break


# ENTRY POINT

if __name__ == "__main__":
    run_chatbot()
