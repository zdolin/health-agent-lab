from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from agents.orchestrator_agent import orchestrator_agent
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

class PatientRequest(BaseModel):
    description: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://health-agent-ui.vercel.app"],
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization", "Accept", "Origin", "X-Requested-With"],
    max_age=3600
)

@app.get("/")
def root():
    return {"status": "ok", "message": f"Last updated: 2025-06-14 21:38:00"}

@app.get("/favicon.ico")
def favicon():
    return {}

@app.options("/triage")
async def options_triage():
    return {"status": "ok"}

@app.post("/triage")
async def stream_response(request: PatientRequest):
    async def generate():
        try:
            last_tool_message = None  # Track the last tool message
            async for event in orchestrator_agent.stream_async(request.description):
                if "data" in event:
                    # Stream text chunks to the client
                    yield event["data"]
                elif "current_tool_use" in event:
                    tool_info = event["current_tool_use"]
                    current_message = None
                    if tool_info["name"] == "triage_tool":
                        current_message = f"\n🔍 Using triage tool to analyze symptoms...\n"
                    elif tool_info["name"] == "rx_lookup_tool":
                        current_message = f"\n💊 Looking up medication information...\n"
                    
                    # Only yield if the message is different from the last one
                    if current_message and current_message != last_tool_message:
                        yield current_message
                        last_tool_message = current_message
                elif "reasoning" in event and event.get("reasoningText"):
                    yield f"\n📝 {event['reasoningText']}\n"
                elif "message" in event:
                    message_content = event.get("message", {})
                    if isinstance(message_content, dict):
                        content = message_content.get("content", "No content")
                        role = message_content.get("role", "unknown")
                        if role == "user":
                            # Handle tool results
                            if isinstance(content, list) and len(content) > 0:
                                for item in content:
                                    if isinstance(item, dict) and 'toolResult' in item:
                                        tool_result = item['toolResult']
                                        if tool_result.get('status') == 'success':
                                            content_list = tool_result.get('content', [])
                                            if isinstance(content_list, list) and len(content_list) > 0:
                                                text_content = content_list[0].get('text', '').strip()
                                                if text_content:
                                                    yield f"\n💬 {text_content}\n"
                            else:
                                yield f"\n💬 {content}\n"
                    else:
                        yield f"\n💬 {message_content}\n"
                elif "force_stop" in event:
                    yield f"\n⚠️ {event.get('force_stop_reason', 'Process stopped')}\n"
        except Exception as e:
            yield f"Error: {str(e)}"

    return StreamingResponse(
        generate(),
        media_type="text/plain",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no"  # Disable proxy buffering
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
