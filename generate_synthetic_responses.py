"""
Utility to generate a privacy-safe synthetic dataset that mimics the structure
expected by `gatundu_poll_analysis.ipynb`. The output intentionally avoids any
real respondent data and only mirrors high-level distributions.
"""

from __future__ import annotations

import random
from datetime import datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

ROWS = 250
OUTPUT_PATH = Path("synthetic_responses.csv")


GENDERS = ["Female", "Male"]
AGE_GROUPS = ["18-24", "25-34", "35-44", "45-54", "55+"]
EDUCATION_LEVELS = ["Primary", "Secondary", "College", "University", "Postgraduate"]
EMPLOYMENT_STATUS = ["Employed", "Self-Employed", "Student", "Unemployed"]
WARDS = ["Ngenda", "Kiganjo", "Kahuguini", "Ndarugu", "Gathugu"]
LIKERT = ["Very Poor", "Poor", "Fair", "Good", "Excellent"]
YES_NO_UNSURE = ["Yes", "No", "Undecided"]
PARTIES = ["Jubilee", "UDA", "Democratic Congress Party", "Chama Cha Kazi", "Undecided/None"]
LEADERS = ["Fred Matiangi", "Kalonzo Musyoka", "Rigathi Gachagua", "William Ruto", "Undecided/None"]
CANDIDATES = ["Njinji Murigi", "Kungu Kibathi", "Moses Kuria", "Undecided"]
NATIONAL_DIRECTION = ["Yes", "No", "Unsure"]
ISSUE_OPTIONS = [
    "Education",
    "Healthcare",
    "Roads & Infrastructure",
    "Jobs & Youth Empowerment",
    "Agriculture/Farming",
    "Water",
    "Security",
]
QUALITY_OPTIONS = ["Development Record", "Honesty", "Accessibility", "Education Level", "Party Affiliation"]


def sample_multi(options: list[str], min_items: int, max_items: int) -> str:
    count = random.randint(min_items, max_items)
    return ", ".join(random.sample(options, count))


def make_row(base_date: datetime) -> dict[str, str]:
    timestamp = base_date + timedelta(minutes=random.randint(0, 60 * 24))
    return {
        "Timestamp": timestamp.isoformat(timespec="seconds"),
        "Gender": random.choice(GENDERS),
        "Age_Group": random.choice(AGE_GROUPS),
        "Education_Level": random.choice(EDUCATION_LEVELS),
        "Employment_Status": random.choice(EMPLOYMENT_STATUS),
        "Ward": random.choice(WARDS),
        "MP_Performance_Rating": random.choice(LIKERT),
        "MP_Represents_Interests_Effectively": random.choice(YES_NO_UNSURE),
        "MP_Should_Be_Reelected": random.choice(YES_NO_UNSURE),
        "Supported_Political_Party": random.choice(PARTIES),
        "Trusted_Political_Leader": random.choice(LEADERS),
        "Preferred_Candidate_If_Election_Today": random.choice(CANDIDATES),
        "President_Ruto_Performance_Rating": random.choice(LIKERT),
        "Country_Heading_Right_Direction": random.choice(NATIONAL_DIRECTION),
        "Top_Voting_Issues": sample_multi(ISSUE_OPTIONS, 2, 4),
        "Important_MP_Qualities": sample_multi(QUALITY_OPTIONS, 1, 3),
    }


def main() -> None:
    random.seed(2025)
    np.random.seed(2025)

    start_date = datetime(2025, 10, 1)
    rows = [make_row(start_date + timedelta(days=i // 10)) for i in range(ROWS)]
    df = pd.DataFrame(rows)

    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Wrote {len(df)} synthetic rows to {OUTPUT_PATH.resolve()}")


if __name__ == "__main__":
    main()

