import json
import ollama

from dataclasses import asdict
from app.analyzer.models import PageAnalysis


def build_analysis_context(analysis: PageAnalysis,) -> dict:

    """ Converts a PageAnalysis object into a dictionary
    that can be sent to an LLM. """

    return asdict(analysis)       #Built-in dataclasses func that converts objects into dictionaries
    #To send a dictionary representing an analyzed page to an LLM


def generate_workflow(analysis: PageAnalysis, user_goal: str,) -> str:

    """
    Entry point for every AI request.
    Uses the local LLM to generate a browser workflow.
    """

    context = build_analysis_context(analysis)

    #f-string (multi-line string hence the """) prompting the llm of what to do
    prompt = f"""You are an expert browser automation planner.

A webpage has already been analyzed.

Website Analysis:


{json.dumps(context, indent=2)}

User Goal:

{user_goal}

Generate ONLY valid JSON.

Format:

{{
  "steps": [
    {{
      "action": "",
      "target": "",
      "value": ""
    }}
  ]
}}
"""

    response = ollama.chat(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response.message.content   #since my installed ollama library returns a Message object