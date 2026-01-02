# Self-Improving Agentic Code Review System

A focused, end-to-end **agentic code review system** designed to assist human reviewers by analyzing pull requests, surfacing potential risks, and improving over time through feedback.

This project intentionally prioritizes **agent orchestration, memory boundaries, and decision-making** over prompt tricks, UI polish, or automation hype.

---

## Problem

Manual code reviews are:
- time-consuming
- cognitively expensive
- inconsistent across teams

Single-agent LLM approaches often fail because:
- long diffs exceed context limits
- mixed concerns reduce reasoning quality
- failures are hard to debug and trust

The result is either **overconfident AI output** or **low-signal suggestions**.

---

## Goal

Build an AI system that:
- **augments** human reviewers instead of replacing them
- highlights **non-obvious risks**, not style issues
- stays reliable under failure
- improves gradually through feedback

The system should **never block developer workflows** and should **degrade gracefully** when AI services are unavailable.

---

## High-Level Architecture

Pull Request Diff
↓
Context Builder
↓
Manager Agent
(task decomposition)
↓
Worker Agents
(focused reviews)
↓
Memory Layer (optional)
↓
Guarded Review Output
↓
Human Reviewer



---

## Agent Roles

### Manager Agent
- Analyzes pull request context
- Identifies review dimensions (e.g. async logic, data access, error handling)
- Decomposes work into focused subtasks
- Assigns tasks to worker agents

**Why:** prevents a single agent from handling too much context and reasoning poorly.

---

### Worker Agents
- Review a narrow concern or file
- Generate **structured, cautious suggestions**
- Return feedback without approval authority

**Why:** smaller context leads to better reasoning and easier validation.

---

### Memory Layer
- Stores historical review feedback
- Enables consistency across multiple reviews
- Used as **advisory context**, not ground truth

Memory is optional and isolated.  
If embeddings or external APIs fail, the system still runs end-to-end.

---

## Design Principles

### Human-in-the-Loop by Design
- The system does **not** approve code
- The system does **not** rewrite logic
- It only surfaces potential risks or questions

Final judgment always belongs to a human reviewer.

---

### Failure-Tolerant AI
External AI services are treated as unreliable by default.

If:
- LLM quota is exceeded
- embeddings are unavailable
- APIs fail

→ the system falls back to safe, deterministic behavior instead of crashing.

---

### Small, Explainable Surface Area
This MVP intentionally avoids:
- UI dashboards
- auto-merge logic
- heavy orchestration infrastructure

The focus is **clarity of reasoning and decision boundaries**, not feature breadth.

---

## Tech Stack

- **Language:** Python
- **LLM:** Llama 3 / OpenAI (pluggable)
- **Agent Orchestration:** LangGraph
- **Memory:** Chroma / Pinecone (optional)
- **Integration:** GitHub API (mocked in MVP)

Tool choices are secondary to system design and tradeoffs.

---

## Running the MVP

```bash
python app/main.py

```
Runs an end-to-end workflow using a mocked pull request diff and prints a guarded review suggestion to the console.

Example Output

Potential risk detected: async behavior introduced.
Consider verifying concurrency safety and error handling.


The output is intentionally:

concise
non-authoritative
risk-focused

Failure Scenarios Handled

Ambiguous tasks → manager narrows scope

Repeated low-quality suggestions → feedback stored

LLM or embedding failures → graceful fallback

No memory available → stateless review still runs


Limitations

No real-time GitHub webhook yet
No human approval interface
Evaluation metrics are minimal
Security hardening not production-ready
These are conscious tradeoffs to keep the system small and explainable.

