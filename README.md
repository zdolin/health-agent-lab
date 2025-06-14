# health-agent-lab
A model-driven agent orchestration prototype using Strands, FastAPI, and Next.js to simulate clinical reasoning tasks with modular, callable tools.

## Docker Setup

### Building the Container
```bash
# Login to ECR
aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <your-account-id>.dkr.ecr.<your-region>.amazonaws.com

# Build the image
docker build -t health-agent-lab .

# Tag the image
docker tag health-agent-lab:latest <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/health-agent-lab:latest

# Push to ECR
docker push <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/health-agent-lab:latest
```

### Running Locally
```bash
docker run -p 8000:8000 health-agent-lab
```

### Environment Variables
The application requires the following environment variables:
- AWS credentials for Bedrock access
- Any other API keys or configuration needed by the agents

You can provide these through:
1. A `.env` file mounted as a volume
2. Environment variables passed to the container
3. AWS ECS task definition environment variables

### ECS Fargate Deployment
To deploy to ECS Fargate:
1. Build and push the Docker image to Amazon ECR
2. Create an ECS cluster
3. Create a task definition with the container image
4. Create a service using the task definition
5. Configure the necessary environment variables in the task definition

The application will be available on port 8000.
