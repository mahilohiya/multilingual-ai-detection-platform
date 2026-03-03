import random
import time

from database import Experiment, SessionLocal


def run_experiment(experiment_id, config):
    db = SessionLocal()
    experiment = db.query(Experiment).filter(Experiment.id == experiment_id).first()

    if not experiment:
        db.close()
        return {"error": "Experiment not found"}

    experiment.status = "running"
    db.commit()

    # Simulated training process (replace with real loop later)
    time.sleep(3)

    accuracy = round(random.uniform(0.75, 0.95), 3)
    loss = round(random.uniform(0.1, 0.4), 3)

    experiment.status = "completed"
    experiment.accuracy = accuracy
    experiment.loss = loss

    db.commit()
    db.close()

    return {
        "accuracy": accuracy,
        "loss": loss,
    }

