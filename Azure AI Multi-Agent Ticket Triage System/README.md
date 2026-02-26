# Azure AI Multi-Agent Ticket Triage System

Production-grade multi-agent system built using Azure AI Foundry.

## Features

- Multi-agent architecture
- Priority classification
- Team assignment
- Effort estimation
- Modular architecture
- Production-ready design

## Tech Stack


- Azure AI Foundry
- Python
- Azure Agents SDK
- Azure Identity

## Run

```bash
pip install -r requirements.txt
cp .env.example .env
python src/main.py
```
---

## Example

##### Input:

>  Users can't login from mobile app

##### Output:

> **Priority**: High
**Team**: Frontend
**Effort**: Medium

---

### Next Level (Recommended Enhancements)

I strongly recommend adding:

- FastAPI backend
- React dashboard
- PostgreSQL storage
- n8n integration
- Azure deployment

---