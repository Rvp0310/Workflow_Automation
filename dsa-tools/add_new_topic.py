import os

BASE = os.path.abspath(os.path.join(os.getcwd(), '../../DSA_solved_problems'))

def create_topic_folder(topic_name, base_dir=BASE):
    topic_dir = os.path.join(base_dir, topic_name)
    difficulties = ["Easy", "Medium", "Hard"]

    if os.path.exists(topic_dir):
        print(f"Folder '{topic_name}' already exists.")
        return

    os.makedirs(topic_dir)
    print(f"Created folder: {topic_dir}")

    for level in difficulties:
        level_path = os.path.join(topic_dir, level)
        os.makedirs(level_path)
        print(f"Created subfolder: {level_path}")

    readme_path = os.path.join(topic_dir, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(f"# {topic_name} Problems\n\n")
        f.write(f"This folder contains solutions to {topic_name.lower()}-related problems categorized by difficulty.\n\n")
        f.write("---\n\n")
        f.write("**None Solved Yet**\n\n")
        f.write("No index Yet\n")

    print(f"Created README.md at: {readme_path}")

if __name__ == "__main__":
    topic = input("Enter topic name: ").strip().title()
    create_topic_folder(topic)
