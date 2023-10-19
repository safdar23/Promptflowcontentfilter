from promptflow import tool

@tool
def blocked_result(question: str, content_safety_check: dict) -> str:
  return f'The question: "{question}" was blocked. <BR> Reason: {content_safety_check["action_by_category"]}'