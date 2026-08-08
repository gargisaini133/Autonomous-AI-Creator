from fastapi import FastAPI
from pydantic import BaseModel
import uuid

from database import create_tables, get_connection


app = FastAPI()

create_tables()


class Persona(BaseModel):
    name: str
    domain: str


class InitRequest(BaseModel):
    persona: Persona


@app.get("/")
def home():
    return {
        "message": "Autonomous AI Creator is running"
    }


@app.post("/api/agent/init")
def initialize_agent(request: InitRequest):
    agent_id = str(uuid.uuid4())

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO agents (agent_id, name, domain) VALUES (?, ?, ?)",
        (
            agent_id,
            request.persona.name,
            request.persona.domain
        )
    )

    conn.commit()
    conn.close()

    return {
        "agentId": agent_id
    }


@app.get("/api/agent/feed")
def get_feed(agentId: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT post_id, created_at, text, rationale, sources
        FROM posts
        WHERE agent_id = ?
        ORDER BY created_at DESC
        """,
        (agentId,)
    )

    rows = cursor.fetchall()
    conn.close()

    posts = []

    for row in rows:
        posts.append({
            "id": row[0],
            "createdAt": row[1],
            "text": row[2],
            "rationale": row[3],
            "sources": row[4].split(",") if row[4] else []
        })

    return {
        "posts": posts
    } 