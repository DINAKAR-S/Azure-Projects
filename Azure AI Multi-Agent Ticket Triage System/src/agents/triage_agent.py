from azure.ai.agents.models import ConnectedAgentTool

def create_triage_agent(client, model, priority, team, effort):

    tools = [
        ConnectedAgentTool(
            id=priority.id,
            name="priority_agent",
            description="Priority analyzer"
        ),
        ConnectedAgentTool(
            id=team.id,
            name="team_agent",
            description="Team assigner"
        ),
        ConnectedAgentTool(
            id=effort.id,
            name="effort_agent",
            description="Effort estimator"
        ),
    ]

    instructions = """
    Coordinate ticket triage.

    Return JSON:
    {
        "priority": "",
        "team": "",
        "effort": ""
    }
    """

    return client.create_agent(
        name="triage-agent",
        model=model,
        instructions=instructions,
        tools=[tool.definitions[0] for tool in tools]
    )