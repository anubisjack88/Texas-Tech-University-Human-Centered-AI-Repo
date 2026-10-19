import re

def analyze_feedback():
    print("=" * 60)
    print("           CUSTOMER FEEDBACK ANALYSIS PROGRAM           ")
    print("=" * 60)

    while True:
        # Accept User Input
        user_input: str = input("\nPlease enter the customer feedback message below:\n> ")

        # Check for empty input
        if not user_input.strip():
            print("\n[Warning] No feedback entered. Please try again.")
            continue

        # Standard Cleaning and Processing
        original_feedback = user_input
        trimmed_feedback = original_feedback.strip()
        lowercased_feedback = trimmed_feedback.lower()

        # Count words (splitting by whitespace)
        words = trimmed_feedback.split()
        word_count = len(words)

        # Count keyword occurrences in lowercased text
        refund_count = lowercased_feedback.count("refund")
        replacement_count = lowercased_feedback.count("replacement")

        # Replace "ASAP" with "as soon as possible" (case-insensitive substitution)
        updated_feedback = re.sub(r"\bASAP\b", "as soon as possible", trimmed_feedback, flags=re.IGNORECASE)

        # Extract the first sentence (everything before the first period)
        if "." in trimmed_feedback:
            first_sentence = trimmed_feedback.split(".")[0].strip()
        else:
            first_sentence = trimmed_feedback.strip()

        # Check for gratitude
        if "thank you" in lowercased_feedback or "thanks" in lowercased_feedback:
            gratitude_status = "Customer expressed gratitude!"
        else:
            gratitude_status = "No gratitude detected."

        # Display Main Results
        print("\n--- ANALYSIS RESULTS ---")
        print(f"Original Feedback:\n  \"{original_feedback}\"")
        print(f"\nTrimmed Feedback:\n  \"{trimmed_feedback}\"")
        print(f"\nTotal Word Count: {word_count} word(s)")
        print(f"Keyword 'refund' count: {refund_count}")
        print(f"Keyword 'replacement' count: {replacement_count}")
        print(f"\nUpdated Feedback (ASAP replaced):\n  \"{updated_feedback}\"")
        print(f"\nFirst Sentence:\n  \"{first_sentence}\"")
        print(f"\nGratitude Status:\n  {gratitude_status}")

        # Advanced Analysis (Extra Credit)
        print("\n--- ADVANCED ANALYSIS (EMPHASIS DETECTION) ---")

        # Split text into sentences while keeping punctuation markers (. ! ?)
        sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", trimmed_feedback) if s.strip()]

        # Matches ALL-CAPS words of 3+ letters OR exclamation marks
        emphasis_pattern = re.compile(r"\b[A-Z]{3,}\b|!")

        found_emphasis = False
        for i, sentence in enumerate(sentences):
            matches = emphasis_pattern.findall(sentence)
            if matches:
                found_emphasis = True
                # Get sentence following current one if it exists
                next_sentence = sentences[i + 1] if i + 1 < len(sentences) else "[None - End of feedback]"

                for match in matches:
                    print(f"\nEmphasized Element: '{match}'")
                    print(f"  • Sentence found in: \"{sentence}\"")
                    print(f"  • Next sentence:     \"{next_sentence}\"")

        if not found_emphasis:
            print("No capitalized words (3+ letters) or exclamation marks (!) detected.")

        # User continuation Loop
        print("\n" + "=" * 60)
        while True:
            choice = input("Continue to analyze another review? (yes/no): ").strip().lower()
            if choice in ['yes', 'y', 'no', 'n']:
                break
            print("Invalid entry. Please enter only 'yes' or 'no'.")

        if choice in ['no', 'n']:
            print("\nThank you for using the Feedback Analysis Program. Goodbye!")
            break


# Execute the main function at the root module level
if __name__ == "__main__":
    analyze_feedback()