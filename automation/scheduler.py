"""
Scheduler — run workflows on a timer (e.g. "every Friday, backup files").

Stub. Suggested implementation: the `schedule` package for simple cases,
or `APScheduler` for more control.
"""


def schedule_daily(time_str: str, workflow_fn):
    # TODO: implement with the `schedule` package, e.g.:
    #   import schedule, time
    #   schedule.every().day.at(time_str).do(workflow_fn)
    #   while True:
    #       schedule.run_pending()
    #       time.sleep(30)
    raise NotImplementedError("Wire up automation/scheduler.py:schedule_daily with the `schedule` package")
