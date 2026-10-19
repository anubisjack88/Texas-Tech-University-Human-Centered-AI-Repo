"""
DoctorTherapyChatbot_Gemar_Johnston.py
HCAI 4302 - Fundamentals of Human-Centered Programming Logic

Project Description: A small "Doctor" chatbot that runs in the terminal.
The bot answers with either:
    (a) a hedge          -> "Please tell me more."
    (b) a qualifier + a reflection of what the user said
        -> "Why do you say that you feel unhappy?"

Things I had to watch out for while building this (the "tricks"):
1. Swapping pronouns one at a time with str.replace() breaks. If you change
    "I" -> "you" and then "you" -> "I", you undo your own work. I go
    word by word and swap each word exactly once.
2. str.replace("my", "your") also hits words like "mystery" or "enemy".
    Working with whole words avoids that.
3. "you" can mean "I" (subject: "you are") or "me" (object: "I hate you").
4. Verbs have to change with the pronoun ("I am" -> "you are",
    "you are" -> "I am", "I was" -> "you were").
5. "quit" has to be the WHOLE message. Someone saying "I want to quit my
    job" should NOT end the session.
6. Blank input, trailing punctuation, curly apostrophes, and Ctrl+C / Ctrl+D.
7. Extra credit: "They are my co-workers." and "We are working with them."
    -> "we" would make the bot sound like it is part of the group, so those
    get special handling with an if / elif / else chain.
"""

import random
import re

# ---------------------------------------------------------------------------
# Canned responses
# ---------------------------------------------------------------------------

HEDGES = [
    "Please tell me more.",
    "I see. Go on.",
    "That sounds important. Can you say more about it?",
    "Hmm, I'm listening. Keep going.",
    "Take your time. What else comes to mind?",
    "I'd like to understand that better.",
    "Okay. How does that sit with you?",
]

# Each qualifier has a {} where the reflected sentence goes.
QUALIFIERS = [
    "Why do you say that {}?",
    "What makes you think that {}?",
    "How long have you felt that {}?",
    "Do you really believe that {}?",
    "I hear you saying that {}. How does that make you feel?",
    "Is it true that {}?",
]

EXIT_WORDS = {"quit", "exit", "bye", "goodbye"}

# ---------------------------------------------------------------------------
# Reflection (pronoun swapping)
# ---------------------------------------------------------------------------

# Words that always swap the same way no matter what's around them.
SWAPS = {
    "i": "you",
    "me": "you",
    "my": "your",
    "mine": "yours",
    "myself": "yourself",
    "i'm": "you're",
    "i've": "you've",
    "i'll": "you'll",
    "i'd": "you'd",
    "your": "my",
    "yours": "mine",
    "yourself": "myself",
    "you're": "I'm",
    "you've": "I've",
    "you'll": "I'll",
    "you'd": "I'd",
}

# If "you" is followed by one of these (or comes first in the sentence, or
# right after one of the PRE words) it is acting as the subject -> "I".
# Otherwise it is the object -> "me". Not perfect, but it handles most cases.
VERBS_AFTER_YOU = {
    "are", "were", "have", "had", "will", "would", "can", "could", "should",
    "do", "did", "don't", "didn't", "cannot", "can't", "won't", "never",
    "always", "just", "really", "make", "made", "seem", "look", "think",
    "know", "want", "need", "feel", "keep", "never", "don't",
}
WORDS_BEFORE_SUBJECT_YOU = {
    "do", "did", "would", "can", "could", "will", "should", "are", "were",
    "if", "that", "because", "think", "believe", "say", "when", "but", "and",
}


def clean_word(word):
    """Lowercase a word and strip punctuation off both ends (keeps apostrophes)."""
    return re.sub(r"^[^\w']+|[^\w']+$", "", word).lower()


def swap_word(low, prev, nxt, is_first):
    """Return the swapped version of one word, or None if it stays the same."""
    if low in SWAPS:
        return SWAPS[low]

    if low == "you":
        if is_first or nxt in VERBS_AFTER_YOU or prev in WORDS_BEFORE_SUBJECT_YOU:
            return "I"
        return "me"

    # verb agreement
    if low == "am":
        return "are"
    if low == "are" and prev == "you":
        return "am"
    if low == "was" and prev == "i":
        return "were"
    if low == "were" and prev == "you":
        return "was"

    return None


def reflect(text):
    """Turn the user's sentence around so the bot can say it back."""
    text = text.replace("\u2019", "'").strip()
    words = text.split()
    result = []

    for i, raw in enumerate(words):
        # split into leading punctuation, the word, and trailing punctuation
        lead, core, trail = re.match(r"^([^\w']*)(.*?)([^\w']*)$", raw).groups()
        low = core.lower()
        prev = clean_word(words[i - 1]) if i > 0 else ""
        nxt = clean_word(words[i + 1]) if i + 1 < len(words) else ""

        new = swap_word(low, prev, nxt, i == 0)

        if new is None:
            # Word stays the same. If it opened the sentence, lowercase it
            # since it's going in the middle of the bot's sentence now.
            # (Downside: a name at the very start gets lowercased too.)
            new = core.lower() if i == 0 else core

        result.append(lead + new + trail)

    # the bot adds its own "?" so drop the user's ending punctuation
    return " ".join(result).rstrip(".!,;:?")


# ---------------------------------------------------------------------------
# Special handling (extra credit)
# ---------------------------------------------------------------------------

def special_case(text):
    """
    Returns a custom reply for sentences the normal reflection handles badly,
    or None if there is nothing special about the input.
    """
    # lowercase, drop apostrophes and punctuation (but keep hyphens so
    # "co-workers" stays "co-workers")
    clean = text.lower().replace("\u2019", "'").replace("'", "")
    clean = re.sub(r"[^\w\s-]", "", clean)
    clean = " ".join(clean.split())

    they_match = re.match(r"^they(?: are|re) my (.+)$", clean)

    if re.match(r"^you(?: are|re) not (?:a |very )?(?:helpful|good)", clean):
        # "You are not a helpful therapist." -> don't just parrot it back
        return random.choice([
            "I'm sorry it feels that way. What would help you more right now?",
            "It sounds like you were hoping for more from me. What are you hoping for?",
        ])

    elif clean == "we are working with them":
        # Reflecting this would give "we are working with them", which sounds
        # like the bot is on the team. The "we" is the user and other people.
        return "Who are you working with, and how is it going?"

    elif they_match:
        group = reflect(they_match.group(1))
        return f"Tell me more about your {group}. How do you get along with them?"

    elif re.search(r"\b(we|us|our|ours)\b", clean):
        # same issue as above for any other sentence with "we"
        return "Who do you mean when you say that? Tell me about the people with you."

    else:
        return None


# ---------------------------------------------------------------------------
# Picking a reply
# ---------------------------------------------------------------------------

last_reply = ""   # so the bot doesn't say the exact same thing twice in a row


def pick(options):
    """random.choice, but not the same thing we just said."""
    global last_reply
    choices = [o for o in options if o != last_reply] or options
    return random.choice(choices)


def get_reply(user_text):
    """Decide what the Doctor says back."""
    global last_reply

    special = special_case(user_text)
    if special is not None:
        last_reply = special
        return special

    # Questions and one-word answers don't reflect well
    # ("Why do you say that how are you?"), so those just get a hedge.
    too_short = len(user_text.split()) < 2
    is_question = user_text.strip().endswith("?")

    if too_short or is_question or random.random() < 0.35:
        reply = pick(HEDGES)
    else:
        qualifier = pick(QUALIFIERS)
        reply = qualifier.format(reflect(user_text))
        # pick() compared the template; compare the final text too
        if reply == last_reply:
            reply = pick(HEDGES)

    last_reply = reply
    return reply


# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------

def main():
    print("Doctor: Hello, I'm the Doctor. What's on your mind today?")
    print("        (Type 'quit' when you want to end the session.)\n")

    while True:
        try:
            user_text = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            # Ctrl+D / Ctrl+C shouldn't dump a traceback on the user
            print("\nDoctor: Take care of yourself. Goodbye.")
            break

        # blank message
        if user_text == "":
            print("Doctor: I'm here whenever you're ready.")
            continue

        # exit only if the WHOLE message is an exit word
        if user_text.lower().strip(" .!") in EXIT_WORDS:
            print("Doctor: Thank you for talking with me today. Take care.")
            break

        print("Doctor:", get_reply(user_text))


if __name__ == "__main__":
    main()
