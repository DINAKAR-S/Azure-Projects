from azure.ai.agents import AgentsClient
from azure.identity import DefaultAzureCredential
from src.config import PROJECT_ENDPOINT

def get_agents_client():

    return AgentsClient(
        endpoint=PROJECT_ENDPOINT,
        credential=DefaultAzureCredential(
            exclude_environment_credential=True,
            exclude_managed_identity_credential=True
        ),
    )