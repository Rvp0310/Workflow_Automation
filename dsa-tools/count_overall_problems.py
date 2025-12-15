import os
import re

BASE = os.path.abspath(os.path.join(os.getcwd(), '../DSA_solved_problems'))

difficulty = {
    'Easy': 0,
    'Medium': 0,
    'Hard': 0
}

def extract_total(readme):
    with open(readme, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith("**Total Solved**:"):
                total = int(line.split(":")[1].strip())
            if line.startswith("- Easy: "):
                val = int(line.split(":")[1].strip())
                difficulty['Easy'] += val
                easy = val
            if line.startswith("- Medium: "):
                val = int(line.split(":")[1].strip())
                difficulty['Medium'] += val
                medium = val
            if line.startswith("- Hard: "):
                val = int(line.split(":")[1].strip())
                difficulty['Hard'] += val
                hard = val
    return (easy, medium, hard, total)

def update_readme():
    topics_done = {}
    for topic_folder in sorted(os.listdir(BASE)):
        path = os.path.join(BASE, topic_folder)
        readme_path = os.path.join(path, "README.md")
        if os.path.isdir(path) and os.path.exists(readme_path):
            counts = extract_total(readme_path) 
            if int(counts[-1]) > 0:
                topics_done[topic_folder] = counts
    
    target = os.path.join(BASE, "README.md")
    with open(target, 'r', encoding='utf-8') as f:
        existing_content = f.read().split('---')[0].strip()  

    topic_list = [f"| *{topic}* | **{counts[0]}** | **{counts[1]}** | **{counts[2]}** | **{counts[3]}** | [./{topic}/README.md](./{topic}/README.md) |" for topic, counts in topics_done.items()]
    topics_section = ("\n| Topic | Easy | Medium | Hard | Total | Path |\n|------|------|--------|------|-------|-------|\n" +"\n".join(topic_list))
    new_content = f"""
---

## Progress Overview

- Total Problems Solved: {sum(counts[3] for counts in topics_done.values())}
    - Easy: {difficulty['Easy']}
    - Medium: {difficulty['Medium']}
    - Hard: {difficulty['Hard']}

---

## Topics Covered

"""
    to_write = existing_content + new_content + topics_section

    with open(target, "w", encoding="utf-8") as f:
        f.write(to_write)

if __name__ == '__main__':
    try:
        update_readme()
        print("Updated The Overall Folder README")
    except Exception as e:
        print("Error:", e)