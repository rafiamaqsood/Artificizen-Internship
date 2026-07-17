#Write a three-step prompt chain using your ask() function: Step 1 extracts action items from a meeting transcript. Step 2 assigns priority (High / Medium / Low) to each. Step 3 formats them as a JSON array. Run all three steps in sequence.

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from wrapper_function import ask

transcript = """
Meeting Transcript:

- Rafia will finish the FastAPI authentication module by Friday.
- Ali should update the project documentation.
- Sara needs to fix the login bug before the next release.
- Ahmed will research vector databases for the RAG project.
- Team will discuss deployment next Monday.
"""

step1_prompt = f"""
Extract only the action items from the following meeting transcript.

Transcript:
{transcript}

Return the action items as a numbered list.
"""

action_items = ask(step1_prompt)

print("===== Step 1: Action Items =====")
print(action_items)


step2_prompt = f"""
Assign a priority (High, Medium, or Low) to each action item.

Action Items:
{action_items}

Return the result as a numbered list.
"""

prioritized_items = ask(step2_prompt)

print("\n===== Step 2: Prioritized =====")
print(prioritized_items)

step3_prompt = f"""
Convert the following prioritized action items into a JSON array.

Each object must contain:
- task
- priority

Prioritized Action Items:
{prioritized_items}

Return ONLY valid JSON.
"""

json_output = ask(step3_prompt)

print("\n===== Step 3: JSON =====")
print(json_output)