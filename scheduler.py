from apscheduler.schedulers.background import BackgroundScheduler

from agent_cycle import run_agent_cycle


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