from datetime import datetime
import random

# ============================================================
#        NOVA - RULE-BASED AI CHATBOT
#        DecodeLabs Internship - Project 1
# ============================================================

BOT_NAME = "Nova"

# ------------------------------------------------------------
# SIMPLE SESSION MEMORY
# ------------------------------------------------------------

user_name = None
message_count = 0


# ------------------------------------------------------------
# PREDEFINED JOKES
# ------------------------------------------------------------

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs! 😂",
    "Why was the computer cold? Because it left its Windows open! 😂",
    "Why did the programmer quit his job? He didn't get arrays! 😂"
]


# ------------------------------------------------------------
# PREDEFINED FACTS
# ------------------------------------------------------------

facts = [
    "Python was created by Guido van Rossum.",
    "AI stands for Artificial Intelligence.",
    "HTML is used to structure web pages.",
    "CSS is used to style web pages.",
    "JavaScript is commonly used to add interactivity to websites."
]


# ------------------------------------------------------------
# MOTIVATIONAL QUOTES
# ------------------------------------------------------------

quotes = [
    "Every expert was once a beginner. 💪",
    "Small progress is still progress. 🚀",
    "Don't stop learning. Your skills grow with practice. 📚",
    "Success comes from consistent effort. 🌟"
]


# ============================================================
# WELCOME MESSAGE
# ============================================================

def show_welcome():

    print("=" * 60)
    print("                 🤖 NOVA AI CHATBOT")
    print("=" * 60)

    print("Hello! I'm Nova, your rule-based AI assistant.")
    print("I can answer predefined questions and help with")
    print("basic AI, programming, study and fun topics.")

    print("\nType 'help' to see what I can do.")
    print("Type 'bye', 'exit', or 'quit' to end the chat.")

    print("=" * 60)


# ============================================================
# HELP MENU
# ============================================================

def show_help():

    print("\n" + "=" * 60)
    print("                 📋 NOVA COMMANDS")
    print("=" * 60)

    print("\n👋 GREETINGS")
    print("  hello | hi | hey")
    print("  good morning | good afternoon | good evening")

    print("\n🤖 CHATBOT")
    print("  who are you")
    print("  what is your name")
    print("  how are you")
    print("  about")

    print("\n🧠 AI TOPICS")
    print("  what is ai")
    print("  what is machine learning")
    print("  what is deep learning")
    print("  what is generative ai")
    print("  what is a chatbot")
    print("  what is an algorithm")

    print("\n💻 PROGRAMMING")
    print("  what is python")
    print("  what is html")
    print("  what is css")
    print("  what is javascript")
    print("  what is programming")
    print("  what is coding")
    print("  what is a variable")
    print("  what is a loop")
    print("  what is if else")

    print("\n📚 STUDY")
    print("  study tips")
    print("  exam tips")
    print("  programming study tips")
    print("  motivation")

    print("\n🧮 CALCULATOR")
    print("  calculate 10 + 5")
    print("  calculate 20 - 5")
    print("  calculate 5 * 4")
    print("  calculate 20 / 4")

    print("\n🕐 UTILITIES")
    print("  time")
    print("  date")
    print("  session")

    print("\n😂 FUN")
    print("  joke")
    print("  fact")
    print("  quote")

    print("\n🚪 EXIT")
    print("  bye | goodbye | exit | quit")

    print("=" * 60)


# ============================================================
# CALCULATOR
# ============================================================

def calculate(expression):

    try:

        expression = expression.replace("calculate", "").strip()

        # Only allow basic mathematical characters
        allowed_characters = "0123456789+-*/(). "

        if not all(character in allowed_characters
                   for character in expression):

            return "I can only calculate basic mathematical expressions."

        result = eval(expression, {"__builtins__": None}, {})

        return f"The answer is {result}. 🧮"

    except ZeroDivisionError:

        return "You cannot divide by zero. ❌"

    except:

        return "I couldn't calculate that. Try something like 'calculate 10 + 5'."


# ============================================================
# MAIN RESPONSE SYSTEM
# ============================================================

def get_response(user_input):

    global user_name
    global message_count

    message_count += 1

    user_input = user_input.lower().strip()

    # --------------------------------------------------------
    # EMPTY INPUT
    # --------------------------------------------------------

    if user_input == "":
        return "Please type something so I can respond. 🙂"

    # --------------------------------------------------------
    # GREETINGS
    # --------------------------------------------------------

    elif user_input in [
        "hello",
        "hi",
        "hey",
        "hii",
        "hello nova"
    ]:

        if user_name:
            return f"Hello again, {user_name}! 👋 How can I help you?"

        else:
            return "Hello! 👋 Nice to meet you. How can I help?"

    elif user_input in ["good morning", "morning"]:

        return "Good morning! ☀️ I hope you have a productive day."

    elif user_input in ["good afternoon", "afternoon"]:

        return "Good afternoon! 😊 What would you like to know?"

    elif user_input in ["good evening", "evening"]:

        return "Good evening! 🌙 How can I help you?"

    # --------------------------------------------------------
    # USER NAME MEMORY
    # --------------------------------------------------------

    elif user_input.startswith("my name is "):

        name = user_input.replace("my name is ", "").strip()

        if name:

            user_name = name.title()

            return (
                f"Nice to meet you, {user_name}! 😊\n"
                "I'll remember your name during this session."
            )

        else:

            return "I didn't catch your name."

    elif user_input in [
        "what is my name",
        "what's my name",
        "do you know my name"
    ]:

        if user_name:

            return f"Your name is {user_name}. 😊"

        else:

            return "You haven't told me your name yet."

    # --------------------------------------------------------
    # HOW ARE YOU
    # --------------------------------------------------------

    elif user_input in [
        "how are you",
        "how are you doing",
        "are you okay"
    ]:

        return (
            "I'm doing great! 🤖\n"
            "I'm ready to help you learn something new!"
        )

    # --------------------------------------------------------
    # CHATBOT INFORMATION
    # --------------------------------------------------------

    elif user_input in [
        "what is your name",
        "what's your name",
        "your name",
        "who are you"
    ]:

        return (
            f"My name is {BOT_NAME}. 🤖\n"
            "I'm a rule-based AI chatbot created using Python."
        )

    elif user_input in [
        "about",
        "about project",
        "project information"
    ]:

        return (
            "This is a Rule-Based AI Chatbot created for "
            "DecodeLabs Internship Project 1.\n"
            "I use predefined responses, if-else decision-making "
            "and a continuous conversation loop."
        )

    # ========================================================
    # AI TOPICS
    # ========================================================

    elif user_input in [
        "what is ai",
        "what is artificial intelligence",
        "define ai"
    ]:

        return (
            "AI stands for Artificial Intelligence. 🧠\n"
            "It is a field of computing focused on creating "
            "systems that can perform tasks that normally "
            "require human intelligence."
        )

    elif user_input in [
        "what is machine learning",
        "define machine learning",
        "what is ml"
    ]:

        return (
            "Machine Learning is a branch of AI where computers "
            "learn patterns from data and use those patterns "
            "to make predictions or decisions."
        )

    elif user_input in [
        "what is deep learning",
        "define deep learning"
    ]:

        return (
            "Deep Learning is a type of machine learning that "
            "uses multi-layer neural networks to learn patterns "
            "from large amounts of data."
        )

    elif user_input in [
        "what is generative ai",
        "define generative ai"
    ]:

        return (
            "Generative AI refers to AI systems that can generate "
            "new content such as text, images, audio or code."
        )

    elif user_input in [
        "what is a chatbot",
        "what is chatbot"
    ]:

        return (
            "A chatbot is a computer program designed to "
            "communicate with users through conversation."
        )

    elif user_input in [
        "what is an algorithm",
        "what is algorithm",
        "define algorithm"
    ]:

        return (
            "An algorithm is a step-by-step set of instructions "
            "used to solve a problem or complete a task."
        )

    # ========================================================
    # PROGRAMMING TOPICS
    # ========================================================

    elif user_input in [
        "what is python",
        "tell me about python",
        "python"
    ]:

        return (
            "Python is a popular programming language known "
            "for its simple and readable syntax. 🐍\n"
            "It is widely used in web development, automation, "
            "data analysis and AI."
        )

    elif user_input in [
        "what is html",
        "define html"
    ]:

        return (
            "HTML stands for HyperText Markup Language. 🌐\n"
            "It is used to structure content on web pages."
        )

    elif user_input in [
        "what is css",
        "define css"
    ]:

        return (
            "CSS stands for Cascading Style Sheets. 🎨\n"
            "It is used to style and design web pages."
        )

    elif user_input in [
        "what is javascript",
        "define javascript"
    ]:

        return (
            "JavaScript is a programming language commonly "
            "used to add interactive behavior to websites."
        )

    elif user_input in [
        "what is programming",
        "programming",
        "what is coding",
        "coding"
    ]:

        return (
            "Programming is the process of writing instructions "
            "that a computer can execute to perform specific tasks."
        )

    elif user_input in [
        "what is a variable",
        "what is variable"
    ]:

        return (
            "A variable is a named location used to store a value "
            "that a program can use and change."
        )

    elif user_input in [
        "what is a loop",
        "what is loop"
    ]:

        return (
            "A loop allows a program to repeat a block of code "
            "multiple times."
        )

    elif user_input in [
        "what is if else",
        "what is if-else",
        "explain if else"
    ]:

        return (
            "An if-else statement allows a program to make decisions.\n"
            "If a condition is true, one block runs; otherwise, "
            "another block can run."
        )

    # ========================================================
    # STUDY TOPICS
    # ========================================================

    elif user_input in [
        "study",
        "studying",
        "study tips",
        "how to study"
    ]:

        return (
            "📚 Study Tips:\n"
            "1. Set a clear study goal.\n"
            "2. Study in focused sessions.\n"
            "3. Take short breaks.\n"
            "4. Practice what you learn.\n"
            "5. Review regularly."
        )

    elif user_input in [
        "exam tips",
        "exam advice",
        "how to prepare for exam"
    ]:

        return (
            "📝 Exam Tips:\n"
            "1. Review important topics.\n"
            "2. Practice past questions.\n"
            "3. Make short notes.\n"
            "4. Manage your time.\n"
            "5. Get enough rest before the exam."
        )

    elif user_input in [
        "programming study tips",
        "how to learn programming"
    ]:

        return (
            "💻 Programming Study Tips:\n"
            "1. Learn the basics first.\n"
            "2. Write code every day.\n"
            "3. Practice small problems.\n"
            "4. Read error messages carefully.\n"
            "5. Build small projects."
        )

    # ========================================================
    # MOTIVATION
    # ========================================================

    elif user_input in [
        "motivate me",
        "motivation",
        "i need motivation"
    ]:

        return random.choice(quotes)

    # ========================================================
    # CALCULATOR
    # ========================================================

    elif user_input.startswith("calculate"):

        return calculate(user_input)

    # ========================================================
    # DATE AND TIME
    # ========================================================

    elif user_input in [
        "time",
        "what time is it",
        "current time",
        "tell me the time"
    ]:

        current_time = datetime.now().strftime("%I:%M %p")

        return f"The current time is {current_time}. 🕐"

    elif user_input in [
        "date",
        "what is today's date",
        "today's date",
        "current date"
    ]:

        current_date = datetime.now().strftime("%d %B %Y")

        return f"Today's date is {current_date}. 📅"

    # ========================================================
    # FUN COMMANDS
    # ========================================================

    elif user_input in [
        "joke",
        "tell me a joke",
        "make me laugh"
    ]:

        return random.choice(jokes)

    elif user_input in [
        "fact",
        "tell me a fact",
        "interesting fact"
    ]:

        return random.choice(facts)

    elif user_input in [
        "quote",
        "give me a quote"
    ]:

        return random.choice(quotes)

    # ========================================================
    # THANK YOU
    # ========================================================

    elif user_input in [
        "thanks",
        "thank you",
        "thank you nova"
    ]:

        return "You're welcome! 😊 I'm happy to help."

    # ========================================================
    # SESSION INFORMATION
    # ========================================================

    elif user_input in [
        "session",
        "session info",
        "how many messages"
    ]:

        return (
            f"You have sent {message_count} messages "
            "during this session. 📊"
        )

    # ========================================================
    # HELP
    # ========================================================

    elif user_input in [
        "help",
        "commands",
        "what can you do"
    ]:

        show_help()

        return ""

    # ========================================================
    # EXIT COMMANDS
    # ========================================================

    elif user_input in [
        "bye",
        "goodbye",
        "exit",
        "quit"
    ]:

        return "__EXIT__"

    # ========================================================
    # UNKNOWN INPUT
    # ========================================================

    else:

        return (
            "I'm sorry, I don't understand that yet. 🤔\n"
            "Type 'help' to see the commands I understand."
        )


# ============================================================
# MAIN CHAT LOOP
# ============================================================

def main():

    show_welcome()

    while True:

        user_input = input("\nYou: ")

        response = get_response(user_input)

        # Exit the chatbot
        if response == "__EXIT__":

            print("\nNova: Goodbye! 👋")
            print("Nova: Thanks for chatting with me.")
            print("Nova: Have a great day! 🚀")

            break

        # Display response
        if response:

            print(f"Nova: {response}")

    print("\n" + "=" * 60)
    print("              CHATBOT SESSION ENDED")
    print("=" * 60)


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()

