# 📝 Advanced Text Summarizer (BART-Based)

This repository contains an advanced text-summarization system built using **HuggingFace BART**, with support for:

✔ Long-text summarization  
✔ Custom sentence count  
✔ Max-word limit per line  
✔ No mid-sentence line breaks  
✔ CLI (terminal) interface  
✔ Clean, readable output formatting  

---

## 🚀 Features

### 🔹 1. Advanced BART Summarization
Uses the state-of-the-art **facebook/bart-large-cnn** model to generate high-quality summaries.

### 🔹 2. Word-limited Lines
Each output line:
- Never exceeds the user-defined max words
- Never breaks sentences in the middle
- Keeps summary readable and structured

### 🔹 3. User Controls
You can specify:
- How many sentences the summary should contain
- Maximum words allowed per line
- Whether to auto-fit long sentences into multiple lines

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/biniyam0960/text-summarizer.git
cd text-summarizer
