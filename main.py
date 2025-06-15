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
            async for event in orchestrator_agent.stream_async(request.description):
                if "data" in event:
                    # Stream text chunks to the client
                    yield event["data"]
                elif "current_tool_use" in event:
                    tool_info = event["current_tool_use"]
                    if tool_info["name"] == "triage_tool":
                        yield f"\n🔍 Using triage tool to analyze symptoms...\n"
                    elif tool_info["name"] == "rx_lookup_tool":
                        yield f"\n💊 Looking up medication information...\n"
                elif "reasoning" in event and event.get("reasoningText"):
                    yield f"\n📝 {event['reasoningText']}\n"
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
