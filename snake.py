import os

github_token = os.getenv("GH_TOKEN")
github_username = "barretot"  # Seu nome de usuário no GitHub

os.system(f"npx github-contributions@latest --token {github_token} --user {github_username}")
