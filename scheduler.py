from apscheduler.schedulers.background import BackgroundScheduler

from agent_cycle import run_agent_cycle
from database import get_connection


scheduler = BackgroundScheduler()


def start_agent_schedule(agent_id, name, domain):
    job_id = f"agent-{agent_id}"

    scheduler.add_job(
        run_agent_cycle,
        trigger="interval",
        hours=3,
        args=[agent_id, name, domain],
        id=job_id,
        replace_existing=True
    )

    if not scheduler.running:
        scheduler.start()

    print(f"Automatic schedule started for {name}")


def resume_existing_agents():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT agent_id, name, domain
        FROM agents
        ORDER BY rowid DESC
        LIMIT 1
    """)

    agent = cursor.fetchone()
    conn.close()

    if agent:
        agent_id, name, domain = agent

        start_agent_schedule(
            agent_id,
            name,
            domain
        )

        print("Restored latest agent schedule")
    else:
        print("No existing agent to restore")