def get_pr_diff():
    # In MVP, mock diff to avoid API complexity
    return """
    + async def process_order():
    +   await save_to_db()
    """
