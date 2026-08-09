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

    cursor.execute(
        "SELECT agent_id, name, domain FROM agents"
    )

    agents = cursor.fetchall()
    conn.close()

    for agent_id, name, domain in agents:
        start_agent_schedule(
            agent_id,
            name,
            domain
        )

    print(f"Restored {len(agents)} agent schedule(s)")