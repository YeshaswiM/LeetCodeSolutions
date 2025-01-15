import pytest
import git

def test_repo_exists():
    repo_path = "./your_repo_path"  # Replace with your repository path
    try:
        repo = git.Repo(repo_path)
        assert repo.is_dirty() == False, "Repository has uncommitted changes"
    except git.InvalidGitRepositoryError:
        pytest.fail("Not a valid git repository")

def test_branch_is_main():
    repo_path = "./your_repo_path"  # Replace with your repository path
    repo = git.Repo(repo_path)
    assert repo.active_branch.name == "main", "Not on the main branch"

def test_recent_commit():
    repo_path = "./your_repo_path"  # Replace with your repository path
    repo = git.Repo(repo_path)
    assert len(list(repo.iter_commits('HEAD', max_count=1))) == 1, "No recent commits"
