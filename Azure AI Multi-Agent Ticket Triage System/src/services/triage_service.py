from azure.ai.agents.models import MessageRole, ListSortOrder
from src.client import get_agents_client
from src.config import MODEL_DEPLOYMENT

from src.agents.priority_agent import create_priority_agent
from src.agents.team_agent import create_team_agent
from src.agents.effort_agent import create_effort_agent
from src.agents.triage_agent import create_triage_agent

def run_triage(ticket: str):

    client = get_agents_client()

    priority = create_priority_agent(client, MODEL_DEPLOYMENT)
    team = create_team_agent(client, MODEL_DEPLOYMENT)
    effort = create_effort_agent(client, MODEL_DEPLOYMENT)

    triage = create_triage_agent(
        client,
        MODEL_DEPLOYMENT,
        priority,
        team,
        effort
    )

    thread = client.threads.create()

    client.messages.create(
        thread_id=thread.id,
        role=MessageRole.USER,
        content=ticket
    )

    run = client.runs.create_and_process(
        thread_id=thread.id,
        agent_id=triage.id
    )

    messages = client.messages.list(
        thread_id=thread.id,
        order=ListSortOrder.ASCENDING
    )

    return messages