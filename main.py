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
    allow_origins=["https://health-agent-ui.vercel.app"],
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "Authorization"],
    allow_credentials=True,
    max_age=3600
)

@app.get("/")
def root():
    return {"status": "ok"}

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
