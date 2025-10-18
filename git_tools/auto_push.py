import os;
import subprocess;

BASE = os.path.abspath(os.path.join(os.getcwd(), '..'))

folder_name = input("Enter the folder name to push (case sensitive): ")

folder_path = os.path.join(BASE, folder_name)

if not os.path.isdir(folder_path):
    print(f"path: {folder_path}" )
    print(f"{folder_name} Folder doesn't exist in the current directory")
    exit()

git_folder = os.path.join(folder_path, ".git")

if not os.path.exists(git_folder):
    subprocess.run(["git", "init"], cwd=folder_path, check = True)

    print("***New Repo Detected***")
    repo_url = input("Paste the repository URL here: ")

    subprocess.run(["git", "remote", "add", "origin", repo_url], cwd=folder_path, check = True)
    subprocess.run(["git", "add", "."], cwd=folder_path, check = True)

    i_commit_message = input("Enter a Initial Commit Message(Excluding 'Initial Commit:'): ").strip()
    subprocess.run(["git", "commit", "-m", f"Initial Commit: {i_commit_message}"], cwd=folder_path, check = True)

    subprocess.run(["git", "push", "-u", "origin", "main"], cwd=folder_path, check = True)
else:
    subprocess.run(["git", "add", "."], cwd=folder_path, check = True)

    commit_message = input("Enter a Commit Message: ").strip()
    subprocess.run(["git", "commit", "-m", commit_message], cwd=folder_path, check = True)

    subprocess.run(["git", "push"], cwd=folder_path, check = True)
