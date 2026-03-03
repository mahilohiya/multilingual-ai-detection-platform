import json

from database import Experiment, SessionLocal
from worker import run_experiment


def create_experiment(config):
    db = SessionLocal()

    experiment = Experiment(
        status="created",
        config=json.dumps(config),
    )

    db.add(experiment)
    db.commit()
    db.refresh(experiment)

    # Run synchronously for now; can be moved to a background worker/queue later
    run_experiment(experiment.id, config)

    db.close()

    return experiment.id


def get_experiment(experiment_id):
    db = SessionLocal()
    experiment = db.query(Experiment).filter(Experiment.id == experiment_id).first()
    db.close()

    if not experiment:
        return None

    return {
        "id": experiment.id,
        "status": experiment.status,
        "accuracy": experiment.accuracy,
        "loss": experiment.loss,
        "config": experiment.config,
    }

