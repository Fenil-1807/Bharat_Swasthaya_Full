def extract_text(content) -> str:
    """
    Normalize LangChain message content into a plain string.

    Handles both:
    - content = "plain string"
    - content = [{'type': 'text', 'text': '...', 'extras': {...}}, ...]
      (Gemini "thinking"-capable models return this block format so
      LangChain has somewhere to attach extra metadata like the
      'signature' field.)
    """
    if isinstance(content, str):
        return content

    if isinstance(content, list):
        text_parts = []
        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
                text_parts.append(block.get("text", ""))
            elif isinstance(block, str):
                text_parts.append(block)
        return "".join(text_parts)

    return str(content) if content is not None else ""