# Zeno — Basic Chatbot

A simple rule-based chatbot built with **pure Python**.  
It responds to greetings, questions, and commands using predefined rules — no external libraries or APIs.

---
## Project Info
| Detail | Info |
|---|---|
| Task - Basic Chatbot |
| Language | Python 3 |
| Libraries Used | `random`, `time` (both built-in) |
| Type | Console / Terminal Application |

---
## Python Concepts Used

| Concept | Where it's applied |
|---|---|
| `if-elif` (keyword matching) | `get_response()` checks the user's input against known keywords |
| `functions` | 5 functions — each handles one specific job |
| `loops` | `while True` keeps the conversation going; `for` loop scans keywords |
| `input / output` | `input()` reads what the user types; `print()` shows the reply |
| `dictionary` | `RESPONSES` stores every keyword and its possible replies |
| `random` | `random.choice()` picks a varied reply so the bot doesn't repeat itself |
| `time` | `time.strftime()` returns the current system time when asked |

---
##  How It Works

1. The chatbot starts and shows a welcome banner
2. You type a message (e.g. `hello`, `tell me a joke`, `what time is it`)
3. The bot scans your message for a known keyword
4. If found, it replies with one of several possible responses
5. If not found, it gives a friendly fallback reply
6. Typing `bye`, `exit`, or `quit` ends the conversation

---
## Supported Commands

| What you type | What Zeno does |
|---|---|
| `hello` / `hi` / `hey` | Greets you back |
| `good morning` / `good night` | Time-of-day reply |
| `how are you` | Checks in |
| `who are you` / `your name` | Introduces itself |
| `what can you do` | Lists its capabilities |
| `tell me a joke` | Tells a programming joke |
| `what time is it` | Shows the current system time |
| `thank you` | Responds politely |
| `help` | Shows all available commands |
| `bye` / `exit` / `quit` | Ends the session |

---
## Demo
```
============================================
           ZENO  —  Basic Chatbot
      Rule-Based Python Conversational AI
============================================
  Type 'help' for commands  |  'bye' to exit
============================================

You   : hello
Zeno  : Hey there! What's on your mind?
--------------------------------------------

You   : tell me a joke
Zeno  : Why do programmers prefer dark mode?
          → Because light attracts bugs!
--------------------------------------------

You   : what time is it
Zeno  : The current time is 03:45 PM.
--------------------------------------------

You   : bye
Zeno  : Goodbye! Have a wonderful day!
--------------------------------------------
```

---
## Program Flow
```
Program starts
      │
      ▼
display_banner()
  → prints the welcome header
      │
      ▼
run_chatbot() — main loop (while True)
  │
  ├── input() captures what the user types
  │
  ├── get_response(user_input)
  │     → loops through RESPONSES dictionary keys
  │     → if a keyword is found inside the input → random.choice() picks a reply
  │     → "time" keyword is replaced live using time.strftime()
  │     → if nothing matches → random fallback reply
  │
  ├── print() displays Zeno's reply
  │
  └── is_exit_command(user_input)
        → checks if the input contains bye / exit / quit
        → if True → loop breaks and chat ends
```

---
## Project Structure
```
CodeAlpha_BasicChatbot/
│
├── chatbot.py       # Main chatbot — all logic in one file
└── README.md        # Project documentation
```

---
## Functions Overview
| Function | What it does |
|---|---|
| `get_response(user_input)` | Matches input against keywords and returns a reply |
| `is_exit_command(user_input)` | Checks if the user wants to end the chat |
| `display_banner()` | Prints the welcome header when the program starts |
| `display_separator()` | Prints a divider line between conversation turns |
| `run_chatbot()` | Runs the main loop — reads input, gets a reply, checks for exit |

---
## Edge Cases Handled

- **Empty input** — prompts the user to type something instead of crashing
- **Unrecognised input** — returns a helpful fallback reply instead of an error
- **Ctrl+C interrupt** — exits cleanly without showing a Python error traceback
- **Case-insensitive matching** — "HELLO", "Hello", and "hello" all work the same

---
## How to Run

```bash
# Make sure Python 3 is installed
python --version

# Run the chatbot
python chatbot.py
```

No installation needed — this project only uses Python's built-in `random` and `time` modules.

---
## Author
SURAJ KUMAR SINGH
