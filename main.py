import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import errors


# Load .env from the same folder as this Python file.
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

API_KEY = os.getenv("GEMINI_API_KEY", "").strip()

if not API_KEY or API_KEY == "PASTE_YOUR_NEW_GEMINI_API_KEY_HERE":
    raise SystemExit(
        "\nGemini API key is missing.\n"
        "1. Create a .env file in the same folder as main.py.\n"
        "2. Add: GEMINI_API_KEY=your_new_api_key\n"
        "3. Save the file and run main.py again.\n"
    )

# The model name below is listed in Google's current Gemini API documentation.
MODEL_NAME = "gemini-3.8-flash"

try:
    client = genai.Client(api_key=API_KEY)
except Exception as exc:
    raise SystemExit(f"Could not initialize Gemini client: {exc}")


def generate_content(prompt: str) -> None:
    """Send a prompt to Gemini and print the generated response."""
    try:
        print("\nGenerating content... Please wait.\n")
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
        )

        result = response.text
        if result:
            print("\n========== AI GENERATED RESULT ==========\n")
            print(result)
            print("\n=========================================\n")
        else:
            print("Gemini returned an empty response. Please try again.")

    except errors.APIError as exc:
        print(f"\nGemini API error: {exc}")
        print(
            "Check that your API key is valid, the model is available "
            "to your account, and your API quota/billing limits are okay.\n"
        )
    except Exception as exc:
        print(f"\nUnexpected error: {exc}\n")


def get_required_input(message: str) -> str:
    """Ask until the user enters a non-empty value."""
    while True:
        value = input(message).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def notes_generator() -> None:
    print("\n===== AI NOTES GENERATOR =====")
    subject = get_required_input("Enter Subject: ")
    topic = get_required_input("Enter Topic: ")

    prompt = f"""
Create simple, accurate, exam-oriented study notes.

Subject: {subject}
Topic: {topic}

Use clear headings and simple language. Include:
1. Introduction
2. Definition
3. Important concepts
4. Features
5. Examples
6. Short conclusion

Do not invent facts. If something is uncertain, say so.
"""
    generate_content(prompt)


def question_generator() -> None:
    print("\n===== AI QUESTION GENERATOR =====")
    subject = get_required_input("Enter Subject: ")
    topic = get_required_input("Enter Topic: ")

    prompt = f"""
Create a practice question set for students.

Subject: {subject}
Topic: {topic}

Include:
1. Five multiple-choice questions, each with four options and the correct answer.
2. Five short-answer questions.
3. Three long-answer questions.

Use simple academic language. Keep the answers clearly labelled.
"""
    generate_content(prompt)


def writing_enhancer() -> None:
    print("\n===== AI WRITING ENHANCER =====")
    print("Enter your academic text. Type END on a new line when finished:")

    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    academic_text = "\n".join(lines).strip()
    if not academic_text:
        print("No text entered. Returning to the main menu.")
        return

    prompt = f"""
Rewrite the following text in formal academic language.

Improve grammar, sentence structure, clarity, coherence, readability,
and academic tone. Preserve the original meaning and do not add
unsupported facts.

Original text:
{academic_text}
"""
    generate_content(prompt)


def research_generator() -> None:
    print("\n===== AI RESEARCH IDEA GENERATOR =====")
    subject = get_required_input("Enter Subject Domain: ")
    keywords = get_required_input("Enter Keywords: ")
    interest = get_required_input("Enter Research Interest: ")

    prompt = f"""
Act as an academic research assistant.

Subject domain: {subject}
Keywords: {keywords}
Research interest: {interest}

Generate:
1. Possible research areas
2. Five interdisciplinary research topics
3. Research objectives
4. A preliminary research outline
5. Suggested research methodology
6. Expected outcomes

Use simple academic language and proper headings.
Distinguish suggestions from established facts.
"""
    generate_content(prompt)


def main() -> None:
    while True:
        print("\n====================================")
        print("          AI STUDY ASSISTANT")
        print("====================================")
        print("\nChoose an option:")
        print("1. AI Notes Generator")
        print("2. AI Question Generator")
        print("3. AI Writing Enhancer")
        print("4. AI Research Idea Generator")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            notes_generator()
        elif choice == "2":
            question_generator()
        elif choice == "3":
            writing_enhancer()
        elif choice == "4":
            research_generator()
        elif choice == "5":
            print("\nThank you for using AI Study Assistant!")
            break
        else:
            print("\nInvalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
