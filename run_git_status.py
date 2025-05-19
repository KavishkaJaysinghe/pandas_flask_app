import subprocess

def run_git_status(repo_path):
    result = subprocess.run(
        ["git", "-C", repo_path, "status"],
        capture_output=True,
        text=True
    )
    print(result.stdout)

# Change this to the path of your Git repo
repo_path = "D:\\myproject\\pandas_flask_app"
run_git_status(repo_path)
