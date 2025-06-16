# Health Agent Lab

A multi-agent orchestration prototype using Strands, FastAPI, and AWS Bedrock to simulate clinical reasoning tasks with modular, callable tools. Integrates with the [openFDA API](https://open.fda.gov/) for evidence-based medication information.

⚠️ **DISCLAIMER**: This is a learning project only. This system is not intended to provide medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for medical decisions.

### View a demo here: [https://health-agent-ui.vercel.app/](https://health-agent-ui.vercel.app/)


## Technology Stack

- **Strands**: Multi-agent orchestration framework for complex clinical reasoning tasks
- **FastAPI**: High-performance backend API framework
- **AWS Bedrock**: Foundation model access for advanced AI capabilities
- **AWS ECS**: Currently deployed manually via AWS CLI to ECS Fargate

## Features

This system provides automated clinical reasoning through a multi-agent architecture that processes patient symptoms, assesses risk levels, and retrieves medication information from the [openFDA API](https://open.fda.gov/). The agents work together to provide structured, evidence-based responses while maintaining clear documentation of all data sources and reasoning steps.

## Architecture

Each agent is designed to handle specific aspects of clinical reasoning, working in concert through the Strands orchestration framework.

The system consists of three main agent types:
1. **Triage Agent**: Specializes in symptom analysis and risk assessment
   - Uses `extract_health_terms` tool to identify medical conditions and symptoms
   - Uses `assess_risk` tool to evaluate severity and urgency
   
2. **RX Agent**: Handles medication information retrieval from openFDA
   - Uses `http_request` tool to query the openFDA API
   - Processes and structures drug information from FDA data
   
3. **Orchestrator Agent**: Manages the workflow and coordinates between agents
   - Combines and structures the final response

## Prerequisites

- Python 3.8+
- AWS Account with Bedrock access
- AWS CLI configured with appropriate credentials

## Setup

1. Clone the repository:
```bash
git clone https://github.com/zdolin/health-agent-lab.git
cd health-agent-lab
```

2. Set up and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure AWS access:
   - Ensure you have AWS CLI installed and configured with appropriate credentials
   - You'll need access to the Claude 3.5 Haiku model in AWS Bedrock (us.anthropic.claude-3-5-haiku-20241022-v1:0)

5. Start the server:
```bash
python main.py
```

The API will be available at http://localhost:8000

## API Endpoints

The main entry point for clinical reasoning is:
- `/triage` - Initiates the multi-agent clinical reasoning process

## License

MIT License
