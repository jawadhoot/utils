import os
from pathlib import Path

url = "https://github.com/jawadhoot/"
repos = ["aatp", "dotcom" , "knockoffmania", "pibot", "pixel-art", "resume", "story-board"]
workspace = Path.home().joinpath("workspace")
print(str(workspace))
if not Path.is_dir(workspace):
  os.mkdir(str(workspace))

for repo in repos:
  repo_dir = workspace.joinpath(repo)
  print(repo_dir)
  os.chdir(workspace)
  if not Path.is_dir(repo_dir.joinpath(".git")):
    os.system("git clone " + url + repo)
  os.chdir(repo_dir)
  os.system("git pull")
  os.system("git push")