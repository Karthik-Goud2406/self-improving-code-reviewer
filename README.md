
# Agentic Code Review System

An autonomous, multi-agent system designed to assist with code reviews by analyzing pull requests, suggesting improvements, and learning from past feedback.

The focus of this project is **agent orchestration, memory, and decision boundaries**, not prompt tricks.

---

## Problem Statement

Manual code reviews are time-consuming and inconsistent.  
Single-agent LLM solutions struggle with long context and complex reasoning.

This system uses **agent decomposition** to improve reliability.

---

## System Architecture

### Agent Roles

1. **Manager Agent**
   - Analyzes pull request context
   - Decomposes review tasks
   - Assigns work to worker agents

2. **Worker Agents**
   - Review specific files or concerns
   - Generate focused suggestions
   - Return structured feedback

3. **Memory Layer**
   - Stores historical feedback
   - Enables iterative improvement over time

---

## Why Multi-Agent?

- Reduces long-context failures
- Improves reasoning quality
- Allows isolation of errors
- Easier to debug and extend

---

## Tech Stack

- **LLM:** Llama 3  
- **Orchestration:** LangGraph  
- **Memory:** Pinecone  
- **Integration:** GitHub API  
- **Backend:** Python

---

## Key Design Decisions

- **Manager–Worker pattern**  
  Prevents a single agent from handling too much context.

- **Structured agent outputs**  
  Makes suggestions easier to validate and apply.

- **Long-term memory**  
  Improves consistency across multiple reviews.

---

## Failure Scenarios Handled

- Ambiguous tasks → manager re-assigns work
- Repeated low-quality suggestions → feedback stored
- API failures → graceful fallback

---

## Limitations & Future Work

- No human-in-the-loop approval yet
- Evaluation metrics are basic
- Security hardening required for enterprise use

---

## Why This Project Exists

To demonstrate **agent orchestration, reasoning boundaries, and memory management** in applied GenAI systems.
