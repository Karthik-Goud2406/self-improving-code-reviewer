Self-Improving Agentic Code Review System

A lean, workflow-driven agentic code review system that assists human reviewers by analyzing pull requests, surfacing potential risks, and learning from past feedback over time.

This project is intentionally focused on agent orchestration, memory boundaries, and decision-making, not prompt tricks or UI polish.

Problem

Manual code reviews are:

time-consuming

cognitively expensive

inconsistent across reviewers

Single-agent LLM solutions often fail because:

long diffs exceed context limits

reasoning degrades with mixed concerns

failures are hard to debug or trust

The result is either overconfident AI suggestions or low-signal noise.

Goal

Design an AI system that:

augments human reviewers instead of replacing them

highlights non-obvious risks, not stylistic changes

stays reliable under failure

improves gradually through feedback

The system should never block a developer workflow and should degrade gracefully when AI services are unavailable.

High-Level Architecture
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

Agent Roles
Manager Agent

Analyzes pull request context

Identifies review dimensions (e.g. async logic, data access, error handling)

Decomposes work into focused subtasks

Assigns tasks to worker agents

Why: prevents a single agent from handling too much context and reasoning poorly.

Worker Agents

Review a narrow concern or file

Generate structured, cautious suggestions

Return feedback without approval authority

Why: smaller context → better reasoning → easier validation.

Memory Layer

Stores past review feedback

Enables consistency across multiple reviews

Used as advisory context, not ground truth

Important: memory is optional and isolated.
If embeddings or external APIs fail, the system still works.

Design Principles
1. Human-in-the-Loop by Design

The system:

does not approve code

does not rewrite logic

only surfaces potential risks or questions

Final judgment always belongs to a human.

2. Failure-Tolerant AI

External AI dependencies are treated as unreliable by default.

If:

LLM quota is exceeded

embeddings are unavailable

APIs fail

→ the system falls back to safe, deterministic signals instead of crashing.

3. Small, Explainable Surface Area

This MVP intentionally avoids:

UI dashboards

webhooks

auto-merge logic

heavy orchestration infra

The goal is clarity of reasoning, not feature breadth.

Tech Stack

Language: Python

LLM: Llama 3 / OpenAI (pluggable)

Agent Orchestration: LangGraph

Memory: Chroma / Pinecone (optional)

Integration: GitHub API (mocked in MVP)

Tooling choices are secondary to system boundaries and tradeoffs.

Running the MVP
python app/main.py


This runs an end-to-end workflow using a mocked PR diff and prints a guarded review suggestion to the console.

Example Output
Potential risk detected: async behavior introduced.
Consider verifying concurrency safety and error handling.


This output is intentionally:

concise

non-authoritative

risk-focused

Failure Scenarios Handled

Ambiguous tasks → manager narrows scope

Repeated low-quality suggestions → feedback stored

LLM / embedding failures → graceful fallback

No memory available → stateless review still runs

Limitations

No real-time GitHub webhook yet

No human approval UI

Evaluation metrics are minimal

Security hardening not production-ready

These are conscious tradeoffs to keep the system small and explainable.

Why This Project Exists

To demonstrate:

agent orchestration under uncertainty

decision boundaries for AI systems

failure-tolerant GenAI design

how AI can augment human judgment, not replace it

This mirrors how I would approach building AI-native systems in a real production environment.
