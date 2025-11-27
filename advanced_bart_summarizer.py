!pip install --quiet transformers==4.39.2 torch

from transformers import pipeline

# -----------------------------
# Load BART summarizer
# -----------------------------
print("Loading BART model on CPU... this may take a while")
bart_summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn",
    framework="pt",
    device=-1
)
print("BART loaded successfully!\n")

# -----------------------------
# Format words into fixed lines
# -----------------------------
def format_lines(words, max_words_per_line):
    lines = []
    for i in range(0, len(words), max_words_per_line):
        line = " ".join(words[i:i+max_words_per_line])
        lines.append(line)
    return "\n".join(lines)

# -----------------------------
# Advanced summarizer
# -----------------------------
def advanced_bart_strict(text, num_sentences=2, total_words=16, max_words_per_line=8):
    # Generate summary using BART
    summary = bart_summarizer(
        text,
        max_length=total_words,
        min_length=total_words,
        do_sample=False
    )[0]['summary_text']
    
    # Split into words
    words = summary.split()
    
    # Force exactly total_words
    if len(words) > total_words:
        words = words[:total_words]
    elif len(words) < total_words:
        # Repeat words if too short (rare case)
        words += words[:total_words - len(words)]
    
    # Format into lines
    formatted_summary = format_lines(words, max_words_per_line)
    return formatted_summary

# -----------------------------
# Infinite loop for user input
# -----------------------------
while True:
    print("\nEnter text to summarize (or type 'exit' to quit):")
    user_text = input()
    if user_text.lower() == "exit":
        print("Exiting...")
        break

    try:
        print("Number of sentences in the summary?")
        num_sentences = int(input())
    except:
        num_sentences = 2

    try:
        print("Maximum total words in the summary?")
        total_words = int(input())
    except:
        total_words = 16

    try:
        print("Maximum words per line?")
        max_words_line = int(input())
    except:
        max_words_line = 8

    summary = advanced_bart_strict(
        user_text,
        num_sentences=num_sentences,
        total_words=total_words,
        max_words_per_line=max_words_line
    )
    print("\n🟢 Advanced BART Summary:\n")
    print(summary)

