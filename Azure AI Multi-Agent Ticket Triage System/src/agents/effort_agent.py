def create_effort_agent(client, model):

    instructions = """
    Estimate effort.

    Return JSON:
    {
        "effort": "Small | Medium | Large",
        "reason": "short explanation"
    }
    """

    return client.create_agent(
        name="effort-agent",
        model=model,
        instructions=instructions
    )