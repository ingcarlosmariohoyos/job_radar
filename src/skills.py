import csv

def load_skills(path):
    skills_by_alias = {}
    with open(path, newline='', encoding='UTF-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            skill_data = {
                "skill": row["skill"],
                "category": row["category"],
                "level": int(row["level"]),
                "evidence": row["evidence"]
            }
            for alias in row["aliases"].split(";"):
                skills_by_alias[alias] = skill_data
    return skills_by_alias

            

skills_by_alias = load_skills('config/skills.csv')
print(skills_by_alias["pbi"])
print(skills_by_alias["plsql"])

