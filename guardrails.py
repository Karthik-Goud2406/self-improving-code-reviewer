def apply_guardrails(text: str):
    if len(text) > 500:
        return text[:500] + "\n\n[Truncated for clarity]"
    return text
