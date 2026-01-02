def build_context(diff: str):
    return {
        "language": "python",
        "risk_hint": "async behavior",
        "diff": diff
    }
