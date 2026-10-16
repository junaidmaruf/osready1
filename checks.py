import subprocess
from pathlib import Path


def run_git(path, *args):
    result = subprocess.run(["git", "-C", path, *args], capture_output=True, text=True)
    return result.stdout.strip()


def check_git_repo(path):
    ok = (Path(path) / ".git").exists()
    return "Git repository", ok, "Run 'git init'"


def check_remote(path):
    ok = bool(run_git(path, "remote", "-v"))
    return "Remote configured", ok, "Run 'git remote add origin <url>'"


def check_identity(path):
    name = run_git(path, "config", "user.name")
    email = run_git(path, "config", "user.email")
    ok = bool(name) and bool(email)
    return "Git identity set", ok, "Set user.name and user.email"


def check_clean_tree(path):
    ok = run_git(path, "status", "--porcelain") == ""
    return "Working tree clean", ok, "Commit or stash your changes"


def check_branch(path):
    branch = run_git(path, "branch", "--show-current")
    ok = branch not in ("main", "master")
    return "On a feature branch", ok, "Create a new branch"


def check_readme(path):
    ok = any(f.name.lower() == "readme.md" for f in Path(path).iterdir() if f.is_file())
    return "README.md present", ok, "Add a README.md"


def check_license(path):
    ok = any(f.name.lower().startswith("license") for f in Path(path).iterdir() if f.is_file())
    return "LICENSE present", ok, "Add a LICENSE file"


CHECKS = [
    check_git_repo,
    check_remote,
    check_identity,
    check_clean_tree,
    check_branch,
    check_readme,
    check_license,
]


def run_all(path):
    return [check(path) for check in CHECKS]
    #just practicing
