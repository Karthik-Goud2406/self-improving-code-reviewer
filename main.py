from dotenv import load_dotenv
load_dotenv()


from github_client import get_pr_diff
from context_builder import build_context
from memory_store import retrieve_memory, store_feedback
from reviewer_agent import review_code
from guardrails import apply_guardrails

diff = get_pr_diff()
context = build_context(diff)
memory = retrieve_memory(context)

raw_review = review_code(context, memory)
final_review = apply_guardrails(raw_review)

print(final_review)

store_feedback(context, final_review)
