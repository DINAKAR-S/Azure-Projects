def create_priority_agent(client, model):

    instructions = """
    Assess urgency of ticket.

    Return JSON:
    {
        "priority": "High | Medium | Low",
        "reason": "short explanation"
    }
    """

    return client.create_agent(
        name="priority-agent",
        model=model,
        instructions=instructions
    )