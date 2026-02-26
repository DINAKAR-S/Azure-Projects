def create_team_agent(client, model):

    instructions = """
    Assign ticket team.

    Return JSON:
    {
        "team": "Frontend | Backend | Infrastructure",
        "reason": "short explanation"
    }
    """

    return client.create_agent(
        name="team-agent",
        model=model,
        instructions=instructions
    )