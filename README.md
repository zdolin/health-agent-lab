# Health Agent Lab

A prototype for a multi-agent system for clinical reasoning and healthcare decision support, built with AI and web technologies. Integrates with FDA data for evidence-based medication information.

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
2. **RX Agent**: Handles medication information retrieval from openFDA
3. **Orchestrator Agent**: Manages the workflow and coordinates between agents

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

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure AWS credentials:
```bash
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_REGION=your_region
```

4. Start the server:
```bash
python main.py
```

The API will be available at http://localhost:8000

## API Endpoints

The main entry point for clinical reasoning is:
- `/triage` - Initiates the multi-agent clinical reasoning process

## Environment Variables

Required environment variables:
- `AWS_ACCESS_KEY_ID`: Your AWS access key
- `AWS_SECRET_ACCESS_KEY`: Your AWS secret key
- `AWS_REGION`: AWS region for Bedrock access

## License

MIT License
