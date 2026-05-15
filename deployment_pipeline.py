import os
import shutil
import random
import subprocess
import time
import datetime

# --- CONFIGURATION ---
BASE_DIR = r"C:\Users\shrit\.gemini\antigravity\scratch\affiliate_pseo_pages"
STAGING_DIR = os.path.join(BASE_DIR, "content_staging")
PUBLIC_DIR = os.path.join(BASE_DIR, "public")
COMMIT_MESSAGES = [
    "Deploy daily content update",
    "Add regional service documentation",
    "Update static resources",
    "Optimize regional pages for local search",
    "Rollout new compliance features in public docs"
]

def run_git_command(command, cwd):
    print(f"Running: {' '.join(command)}")
    result = subprocess.run(command, cwd=cwd, capture_output=True, text=True, shell=True)
    if result.returncode != 0:
        print(f"Git command failed: {result.stderr}")
    return result

def deploy():
    print(f"[{datetime.datetime.now()}] Triggered deployment script.")
    
    # 1. Random delay (simulating cron running unpredictably if executed strictly at 8am)
    max_delay_seconds = 3 * 60 * 60
    delay = random.randint(0, max_delay_seconds)
    print(f"[{datetime.datetime.now()}] Sleeping for {delay // 60} minutes to ensure organic timing...")
    time.sleep(delay)
    
    print(f"[{datetime.datetime.now()}] Resuming deployment process...")
    
    # 2. Check Staging
    if not os.path.exists(STAGING_DIR):
        print("Staging directory does not exist. Exiting.")
        return
        
    staging_files = [f for f in os.listdir(STAGING_DIR) if f.endswith('.html')]
    
    if not staging_files:
        print(f"[{datetime.datetime.now()}] SUCCESS: /content_staging/ is empty. All pages have been fully deployed.")
        return

    # 3. Select 15-25 files
    num_to_deploy = random.randint(15, 25)
    files_to_deploy = random.sample(staging_files, min(num_to_deploy, len(staging_files)))
    
    print(f"Selected {len(files_to_deploy)} files to deploy.")
    
    # 4. Move files to public
    if not os.path.exists(PUBLIC_DIR):
        os.makedirs(PUBLIC_DIR)
        
    for f in files_to_deploy:
        src = os.path.join(STAGING_DIR, f)
        dst = os.path.join(PUBLIC_DIR, f)
        shutil.move(src, dst)
        
    # 5. Git Operations
    print("Executing version control operations...")
    run_git_command(["git", "add", "."], cwd=BASE_DIR)
    
    commit_msg = random.choice(COMMIT_MESSAGES)
    run_git_command(["git", "commit", "-m", commit_msg], cwd=BASE_DIR)
    
    run_git_command(["git", "push"], cwd=BASE_DIR)
    
    print(f"[{datetime.datetime.now()}] Deployment complete. {len(staging_files) - len(files_to_deploy)} files remaining in staging.")

if __name__ == "__main__":
    deploy()
