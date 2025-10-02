import os
import re

BASE = os.path.abspath(os.path.join(os.getcwd(), '../DSA_solved_problems'))

def extract_details(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.search(r'/\*.*?\*/', content, re.DOTALL)
    if not match:
        return None

    comment = match.group()
    date = re.search(r'Date:\s*(.*)', comment)
    platform = re.search(r'Platform:\s*(.*?)\s*\((.*?)\)', comment)
    problem_statement = re.search(r'Problem Statement:\s*(.*?)\n[-]+', comment, re.DOTALL)

    return {
        'date': date.group(1).strip() if date else 'N/A',
        'platform_name': platform.group(1).strip() if platform else 'N/A',
        'platform_link': platform.group(2).strip() if platform else '#',
        'problem_statement': problem_statement.group(1).strip() if problem_statement else 'N/A',
    }

def generate_index(TOPIC_DIR):
    table = [
        "\n---\n",
        "### Problem Index\n",
        "| Problem | Platform | Difficulty | Date | Link |",
        "|---------|----------|------------|------|------|"
    ]
    diff = {
        "Easy" : 0,
        "Medium": 0,
        "Hard": 0
    }

    for difficulty in sorted(os.listdir(TOPIC_DIR)):
        diff_path = os.path.join(TOPIC_DIR, difficulty)
        if not os.path.isdir(diff_path): continue

        for problem_folder in sorted(os.listdir(diff_path)):
            prob_path = os.path.join(diff_path, problem_folder)
            if not os.path.isdir(prob_path): continue

            cpp_files = [f for f in os.listdir(prob_path) if f.endswith('.cpp')]
            if not cpp_files: continue

            diff[difficulty] += len(cpp_files)
            cpp_path = os.path.join(prob_path, cpp_files[0])
            details = extract_details(cpp_path)
            if not details: continue

            table.append(
                f"| `{re.sub(r'(?<!^)(?=[A-Z])', ' ', problem_folder.split('_')[1])}` | {details['platform_name']} | {difficulty} | {details['date']} | [Link]({details['platform_link']}) |"
            )

    return '\n'.join(table), diff

def update_readme(topic):
    TOPIC_DIR = os.path.join(BASE, topic)
    README_PATH = os.path.join(TOPIC_DIR, 'README.md')
    with open(README_PATH, 'r', encoding='utf-8') as f:
        existing_content = f.read().split('---')[0].strip()

    table, difficulty = generate_index(TOPIC_DIR)
    index_content = f"""

---
        
**Total Solved**: {difficulty['Easy'] + difficulty['Medium'] + difficulty['Hard']}
- Easy: {difficulty['Easy']}
- Medium: {difficulty['Medium']}
- Hard: {difficulty['Hard']}
"""
    new_content = existing_content + index_content + table

    with open(README_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print("README.md updated with problem index.")

if __name__ == '__main__':
    t = input("Enter the  topic name: ")
    update_readme(t)
