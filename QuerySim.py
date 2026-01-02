import os
import csv
import random
from datetime import datetime
from google import genai  # ensure google-genai is installed
# --- helper functions from your earlier code (slightly fixed) ---

GOOGLE_API_KEY = "AIzaSyD84B0ymczBvDBDrYDkqPfzpeYHjuyKeYY"


def gemini_response(prompt: str) -> str:
    """
    Send prompt to Gemini and return text result.
    Requires GOOGLE_API_KEY in environment.
    """
    try:
        client = genai.Client(api_key=GOOGLE_API_KEY)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        # response.text is expected to be the string result
        # Some SDKs return different shapes; adapt if needed.
        return getattr(response, "text", str(response))
    except Exception as e:
        return f"ERROR calling Gemini: {e}"


def evaluate_performance(transcript: str) -> str:
    """
    Build evaluation prompt and return Gemini's raw response text.
    """
    prompt = f"""
You are an expert evaluator for intern interviews. Evaluate the following conversation transcript.

TRANSCRIPT:
{transcript}

Criteria:
1. Professionalism
2. Grammar and Clarity
3. Relevance of answers

Output strictly in this format:
Score: [Score out of 100]
Feedback: [Brief summary of feedback]
"""
    return gemini_response(prompt)


def parse_evaluation(eval_text: str):
    """Extract score and feedback from Gemini's response text (best-effort)."""
    score = "N/A"
    feedback = eval_text.strip()

    lines = eval_text.splitlines()
    for line in lines:
        if "Score:" in line:
            score = line.split("Score:", 1)[1].strip()
        if "Feedback:" in line:
            feedback = line.split("Feedback:", 1)[1].strip()

    return score, feedback

# --- small CSV reader and random picker ---


def load_questions(csv_path):
    """
    Load CSV once and return list of rows (dicts).
    CSV is expected to have headers: 'question' and 'follow_up_question'
    (exact header names). Keep it simple per your request.
    """
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader if row.get("question")]
    if not rows:
        raise ValueError(
            "No questions found or CSV missing 'question' header.")
    return rows


def pick_random_nonrepeat(rows, count=1):
    """Pick `count` random rows without repetition from list `rows` (returns list)."""
    if count >= len(rows):
        # if requested count >= available, just shuffle and return all
        random.shuffle(rows)
        return rows[:count]
    picks = random.sample(rows, count)
    return picks

# --- utility to read multiline candidate answer ---


def read_multiline_answer(prompt_msg="Type answer. Finish by writing SUBMIT on a new line."):
    print(prompt_msg)
    print("(When done, type a single line with: SUBMIT )")
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            # fallback if input stream closed
            break
        if line.strip() == "SUBMIT":
            break
        lines.append(line)
    return "\n".join(lines).strip()

# --- main simulation loop ---


def main(csv_path="questions.csv", questions_to_ask=3):
    # 1) gather sim taker info
    sim_taker = input("Enter the name of the simulation taker: ").strip()
    if not sim_taker:
        sim_taker = "Unknown"

    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Session started for {sim_taker} at {start_time}")
    print("-" * 40)

    # 2) load questions
    rows = load_questions(csv_path)
    # choose questions_to_ask non-repeating rows
    picks = pick_random_nonrepeat(rows, count=min(questions_to_ask, len(rows)))

    for idx, row in enumerate(picks, start=1):
        question = row.get("question", "").strip()
        follow_up = row.get("follow_up_question", "").strip() or None

        print(f"\nQuestion #{idx}: {question}\n")

        # ask main question, read answer with confirmation loop
        while True:
            answer = read_multiline_answer(
                "Enter candidate's answer (multiline).")
            print("\n--- Candidate's Answer Preview ---")
            print(answer if answer else "[no text entered]")
            confirm = input("Submit this answer? (y/n): ").strip().lower()
            if confirm == "y":
                break
            else:
                print("Okay — re-enter the answer. Finish with SUBMIT when ready.")

        # follow-up if present
        follow_answer = None
        if follow_up:
            print(f"\nFollow-up question: {follow_up}\n")
            while True:
                follow_answer = read_multiline_answer(
                    "Enter candidate's answer to follow-up.")
                print("\n--- Candidate's Follow-up Answer Preview ---")
                print(follow_answer if follow_answer else "[no text entered]")
                confirm = input(
                    "Submit this follow-up answer? (y/n): ").strip().lower()
                if confirm == "y":
                    break
                else:
                    print(
                        "Okay — re-enter the follow-up answer. Finish with SUBMIT when ready.")

        # build transcript
        transcript_lines = []
        transcript_lines.append(f"Interviewer: {question}")
        transcript_lines.append(
            f"Candidate: {answer if answer else '[no answer]'}")
        if follow_up:
            transcript_lines.append(f"Interviewer (follow-up): {follow_up}")
            transcript_lines.append(
                f"Candidate: {follow_answer if follow_answer else '[no answer]'}")

        transcript = "\n".join(transcript_lines)
        print("\nSending transcript to evaluator (Gemini)...")
        eval_text = evaluate_performance(transcript)

        # if eval_text contains an error string returned by gemini_response, print and continue
        if eval_text.startswith("ERROR"):
            print(eval_text)
            print("Skipping parsing due to error. Continue to next question.")
        else:
            score, feedback = parse_evaluation(eval_text)
            print("\n=== Evaluation Result ===")
            print(f"Score: {score}")
            print(f"Feedback: {feedback}")
            print("=========================")

    end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\nSession ended for {sim_taker} at {end_time}")
    print("All done — you asked", len(picks), "questions.")


# run main if this script executed directly
if __name__ == "__main__":
    # change the CSV path here if needed
    CSV_PATH = "questions.csv"
    main(csv_path=CSV_PATH, questions_to_ask=3)
