#!/usr/bin/env python
"""OPENCLAW-ED Crew entry point. Kickoff expects inputs={'ed_state': <dict>}."""
import json
import sys
from openclaw_ed.crew import OpenclawEdCrew


def run():
    """Run the crew with sample inputs (used by `crewai run` locally)."""
    sample = {
        "now": "2026-05-18T22:00:00Z",
        "bed_count": 30,
        "patients": [
            {
                "bed": "B-04", "name": "Nancy Rhodes", "age": 67, "sex": "F",
                "esi": 2, "chief_complaint": "suspected sepsis",
                "arrival_time": "2026-05-18T18:20:00Z",
                "discharge_ready": False, "septic_trajectory": True,
                "vitals": {"hr": 129, "sbp": 93, "dbp": 51, "rr": 27, "spo2": 93, "temp_c": 39.2},
                "orders": [
                    {"name": "Lactate", "placed_at": "2026-05-18T18:35:00Z",
                     "resulted_at": "2026-05-18T19:02:00Z", "read_at": None,
                     "abnormal": True, "critical": True},
                ],
            }
        ],
        "waiting_room": [],
    }
    result = OpenclawEdCrew().crew().kickoff(inputs={"ed_state": sample})
    print(result)


def kickoff():
    run()


if __name__ == "__main__":
    run()
