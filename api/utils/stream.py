import json
from fastapi.responses import StreamingResponse

def patch_response_with_headers(response: StreamingResponse, protocol: str):
    if protocol == "text":
        response.headers["x-vercel-ai-data-stream"] = "v1"
    return response

async def stream_text(client, messages, tool_definitions, available_tools, protocol):
    # Basic implementation
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        stream=True,
    )
    
    for chunk in completion:
        if chunk.choices[0].delta.content:
            text = chunk.choices[0].delta.content
            if protocol == "text":
                yield text
            else:
                # Default "data" protocol or others - simplified for now
                yield f'0:{json.dumps(text)}\n'
