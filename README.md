# Python-Error-Fixer
# 🐍 Python-Error-Fixer

> **An LLM-Powered Agent for Automated Single-Line Bug Repair in Python Programs from the QuixBugs Benchmark**  
> **Created for AIMS-DTU Research Internship Round 2 — Automated Code Correction Task**

---

## 🔍 Overview

**Python-Error-Fixer** is an intelligent debugging system that leverages the power of large language models to automatically identify and repair **single-line bugs** in Python programs. It focuses on defective implementations drawn from the [QuixBugs Benchmark](https://github.com/RumbleJack56/Code-Refactoring-QuixBugs), a collection of classic algorithmic problems with known bugs.

This project demonstrates a fully functional prototype, featuring a Gradio-based interface, bug classification heuristics, automated test validation, and complete program evaluation with detailed logging.

---

## 🧠 How It Works

### 🧩 Key Components

- ✅ **Model-Driven Repair**: Uses **FLAN-T5** (`google/flan-t5-small`) to fix code.
- 🧪 **Automated Test Execution**: Uses test functions to validate each fix.
- 🏷️ **Bug Classification**: Heuristic bug class mapping from error patterns.
- 🌐 **Gradio UI**: Interactive interface for user-driven or file-based debugging.
- 📈 **Evaluation Pipeline**: Batch processes all programs and logs results.

---

## 📁 Project Structure

.
├── app.py # Core logic: bug fixing, classification, test running
├── evaluate.py # Batch evaluation of all buggy programs
├── results.txt # Output log of evaluation with success/fail reports
├── Code-Refactoring-QuixBugs/
│ └── python_programs/ # Buggy Python implementations from QuixBugs
├── requirements.txt # Required dependencies
└── README.md # This file


🧪 Batch Evaluation

🐞 Bug Classes (Heuristic Mapping)
The system uses string heuristics to classify bugs into 14 common types:

Off-by-one

Incorrect condition

Wrong operator

Wrong return

Wrong assignment

Missing initialization

Extra statement

Infinite loop

Wrong function call

Missing edge case

Logic bug

Data structure misuse

API misuse

Syntax error

These labels help in tracking and potentially adapting future repair strategies.

🔬 Model & Prompt
Model Used: google/flan-t5-small
Prompt Format:

css
Copy
Edit
You are an expert Python developer. The following Python code has a single-line bug:
<code block> ``` Please identify and fix the bug, preserving the original algorithm and style. Return ONLY the fixed code inside a ```python ... ``` code block. ```

🔮 Future Work
 Improve Prompt Engineering: Restrict output to valid Python only.

 Handle Multi-Line Bugs: Extend beyond single-line fixes.

 Cross-Language Support: Add Java support from QuixBugs dataset.

 Custom Metrics: Better evaluate repair quality beyond pass/fail.

📜 License
MIT License. See LICENSE for details.

🙌 Acknowledgments
Dataset: Code-Refactoring-QuixBugs

Model: FLAN-T5

Interface: Gradio
