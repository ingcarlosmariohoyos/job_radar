"""Load the skills dictionary (config/skills.csv) used to match job offers."""

import csv


def load_skills(path):
    """Read the skills CSV and return a dict mapping each alias to its skill data.

    Example: load_skills("config/skills.csv")["pbi"]
    -> {'skill': 'power_bi', 'category': 'bi', 'level': 3, 'evidence': 'work'}
    """
    skills_by_alias = {}
    # newline='' is what the csv docs recommend; utf-8 avoids accent issues on Windows
    with open(path, newline='', encoding='UTF-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            # Cast level to int once, at load time, so scoring can compare numbers
            skill_data = {
                "skill": row["skill"],
                "category": row["category"],
                "level": int(row["level"]),
                "evidence": row["evidence"]
            }
            # Aliases are ';'-separated; every alias points to the same skill_data
            for alias in row["aliases"].split(";"):
                skills_by_alias[alias] = skill_data
    return skills_by_alias


# Manual check (next step: move under `if __name__ == "__main__":`)
skills_by_alias = load_skills('config/skills.csv')
print(skills_by_alias["pbi"])
print(skills_by_alias["plsql"])
