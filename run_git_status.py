# run_git_status.py
import subprocess

# Set the path to your Git repository
repo_path = "D:/myproject/pandas_flask_app"  # change this path as needed

# Get git status
def git_status(repo_path):
	result = subprocess.run(
		["git", "-C", repo_path, "status"],
		capture_output=True, text=True
	)
	return result.stdout

status = git_status(repo_path=repo_path)

# Print the status
print("Git Status Output:")
print(status)
