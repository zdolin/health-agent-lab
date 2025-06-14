from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from agents.orchestrator_agent import orchestrator_agent

app = FastAPI()

class PatientRequest(BaseModel):
    description: str

@app.post("/triage")
async def stream_response(request: PatientRequest):
    async def generate():
        try:
            async for event in orchestrator_agent.stream_async(request.description):
                if "data" in event:
                    # Only stream text chunks to the client
                    yield event["data"]
        except Exception as e:
            yield f"Error: {str(e)}"

    return StreamingResponse(
        generate(),
        media_type="text/plain"
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
