import os
import re

BASE = os.path.abspath(os.path.join(os.getcwd(), '../DSA_solved_problems'))
difficulty = {
    'Easy': 0,
    'Medium': 0,
    'Hard': 0
}

def extract_total(readme):
    total = 0
    with open(readme, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith("**Total Solved**:"):
                total = int(line.split(":")[1].strip())
            if line.startswith("- Easy: "):
                difficulty['Easy'] += int(line.split(":")[1].strip())
            if line.startswith("- Medium: "):
                difficulty['Medium'] += int(line.split(":")[1].strip())
            if line.startswith("- Hard: "):
                difficulty['Hard'] += int(line.split(":")[1].strip())
    return total

def update_readme():
    topics_done = {}
    for topic_folder in sorted(os.listdir(BASE)):
        path = os.path.join(BASE, topic_folder)
        readme_path = os.path.join(path, "README.md")
        if os.path.isdir(path) and os.path.exists(readme_path):
            total = extract_total(readme_path) 
            if total > 0:
                topics_done[topic_folder] = total
    
    target = os.path.join(BASE, "README.md")
    with open(target, 'r', encoding='utf-8') as f:
        existing_content = f.read().split('---')[0].strip()  

    topic_list = [f"- [**{count}**] {topic} (./{topic}/README.md)" for topic, count in topics_done.items()]
    topics_section = "\n".join(topic_list)
    new_content = f"""
---

## Progress Overview

- Total Problems Solved: {sum(topics_done.values())}
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