import os
from pathlib import Path

url = "https://github.com/jawadhoot/"
repos = ["aatp", "dotcom" , "knockoffmania", "pibot", "pixel-art", "resume", "story-board"]
workspace = Path.home().joinpath("workspace")
print(str(workspace))
os.system("mkdir " + str(workspace))

for repo in repos:
  repo_dir = str(workspace.joinpath(repo))
  print(repo_dir)
  os.system("git clone " + url + repo + " " + repo_dir)
  os.chdir(repo_dir)
  os.system("git pull")
  os.system("git push")