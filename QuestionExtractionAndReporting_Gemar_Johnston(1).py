"""
QuestionExtractionAndReporting_Gemar_Johnston.py
HCAI 4302 - Fundamentals of Human-Centered Programming Logic

Reads customer_feedback.txt (one feedback per line, formatted "Name || feedback"),
pulls out every sentence that is a question, and writes them to a report file
along with the customer's name.

Stuff I had to watch for:
  - Splitting on "." does NOT cleanly separate sentences. Some chunks end up
    with a "?" in the MIDDLE, like
        "However, I do have one question about its features? I hope you can
         clarify this for me whenever you get the chance"
    Only the text BEFORE the "?" is the question. The leftover text after it
    is a different sentence and is not a question, so it gets thrown out.
  - A chunk can hold more than one question, so I loop over every "?" part.
  - Sentences that end in "!" can get stuck onto the front of a question
    ("Thanks! Is it ok?"), so I trim anything before the last "!".
  - The file has curly apostrophes (I'm, I'll), so it has to be opened as UTF-8
    or Windows can garble it / crash.
  - Blank lines or lines with no "||" would break the split, so I skip them.
  - Known limit: splitting on "." will break up decimals like "2.5 inches".
    The sample file doesn't have any, so I kept the split(".") approach.
"""

import os

# Look for the files next to this script, so it works no matter where
# the terminal is currently open.
folder = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(folder, "customer_feedback.txt")
REPORT_FILE = os.path.join(folder, "questions_report_Gemar_Johnston.txt")


def extractQuestions(feedback):
    """Return a list of the questions found inside one feedback string."""
    questions = []

    for sentence in feedback.split("."):
        if "?" not in sentence:
            continue

        # Every piece followed by a "?" is a question. The very last piece
        # (after the final "?") never was, so [:-1] leaves it out.
        pieces = sentence.split("?")
        for piece in pieces[:-1]:
            if "!" in piece:
                piece = piece.split("!")[-1]   # drop an "!" sentence stuck on the front
            piece = piece.strip()
            if piece != "":
                questions.append(piece + "?")

    return questions


def main():
    # ---- read the input file ----
    try:
        f = open(INPUT_FILE, "r", encoding="utf-8-sig")
    except FileNotFoundError:
        print(f"Error: couldn't find '{INPUT_FILE}'.")
        print("Make sure customer_feedback.txt is in the same folder as this script.")
        return
    lines = f.readlines()
    f.close()

    questionNumber = 0       # numbers the questions in the report
    totalFeedbacks = 0       # extra credit: how many feedbacks were read
    feedbacksWithQuestions = 0
    reportLines = []

    for line in lines:
        line = line.strip()
        if line == "":
            continue                              # blank line

        if "||" not in line:
            print(f"Skipping a line with no '||' in it: {line[:40]}...")
            continue

        # split once so a stray "||" inside the feedback can't break the unpack
        name, feedback = line.split("||", 1)
        name = name.strip()
        totalFeedbacks += 1

        found = extractQuestions(feedback)
        if len(found) > 0:
            feedbacksWithQuestions += 1

        for q in found:
            questionNumber += 1
            reportLines.append(f"Question {questionNumber}")
            reportLines.append(f"  Customer: {name}")
            reportLines.append(f"  Question: {q}")
            reportLines.append("")

    # ---- write the report ----
    out = open(REPORT_FILE, "w", encoding="utf-8")
    out.write("CUSTOMER QUESTIONS REPORT\n")
    out.write("=" * 50 + "\n\n")

    if questionNumber == 0:
        out.write("No questions were found in the feedback.\n\n")
    else:
        out.write("\n".join(reportLines) + "\n")

    out.write("=" * 50 + "\n")
    out.write(f"Total feedbacks in file:             {totalFeedbacks}\n")
    out.write(f"Feedbacks that contained a question: {feedbacksWithQuestions}\n")
    out.write(f"Total questions extracted:           {questionNumber}\n")
    out.close()

    print(f"Success! The report was generated: {os.path.basename(REPORT_FILE)}")
    print(f"({totalFeedbacks} feedbacks read, {questionNumber} questions extracted)")


if __name__ == "__main__":
    main()
