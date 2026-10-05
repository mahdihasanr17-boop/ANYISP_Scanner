import urllib.request
import json
import subprocess
import os

token = "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"
headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "python-urllib"
}

try:
    # Get user info
    req = urllib.request.Request("https://api.github.com/user", headers=headers)
    res = urllib.request.urlopen(req)
    user_data = json.loads(res.read())
    username = user_data["login"]
    print(f"Logged in as {username}")

    # Create Repo
    repo_name = "ANYISP_Scanner"
    repo_data = json.dumps({
        "name": repo_name,
        "description": "ANYISP Scanner",
        "private": True
    }).encode("utf-8")
    
    try:
        req2 = urllib.request.Request("https://api.github.com/user/repos", data=repo_data, headers=headers, method="POST")
        res2 = urllib.request.urlopen(req2)
        print(f"Repository {repo_name} created successfully.")
    except urllib.error.HTTPError as e:
        if e.code == 422: # Already exists
            print("Repository already exists. Proceeding with push...")
        else:
            raise e
            
    # Git commands
    remote_url = f"https://{token}@github.com/{username}/{repo_name}.git"
    
    subprocess.run(["git", "remote", "remove", "origin"], capture_output=True)
    subprocess.run(["git", "remote", "add", "origin", remote_url], check=True)
    
    # Try changing branch to main if not already
    subprocess.run(["git", "branch", "-M", "main"], check=True)
    
    subprocess.run(["git", "add", "."], check=True)
    
    status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    if status.stdout.strip():
        subprocess.run(["git", "commit", "-m", "Initial upload"], check=True)
    
    print("Pushing to GitHub...")
    push_result = subprocess.run(["git", "push", "-u", "origin", "main"], capture_output=True, text=True)
    if push_result.returncode == 0:
        print(f"Successfully pushed to https://github.com/{username}/{repo_name}")
    else:
        print(f"Git push failed: {push_result.stderr}")

except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code} - {e.read().decode('utf-8')}")
except Exception as e:
    print(f"Error: {e}")
