from strands.models import BedrockModel

# Create the Bedrock model configuration
bedrock_model = BedrockModel(
    model_id="us.anthropic.claude-3-5-haiku-20241022-v1:0",  
    region_name="us-east-1", 
    temperature=0.2,
)