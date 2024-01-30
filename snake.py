import requests
import json
import io
from PIL import Image, ImageDraw

# Configurações
username = "barretot"
token = "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"
repo = "barretot"

# Obter os últimos commits
url = f"https://api.github.com/repos/{username}/{repo}/commits?per_page=100"
headers = {"Authorization": f"token {token}"}
response = requests.get(url, headers=headers)
commits = json.loads(response.content)

# Criar a imagem
width = 400
height = 400
margin = 20
cell_size = 20

image = Image.new("RGB", (width, height), color=(255, 255, 255))
draw = ImageDraw.Draw(image)

# Desenhar a cobrinha
snake_x = margin
snake_y = margin
snake_length = 10
snake_direction = "right"

for i in range(snake_length):
    draw.rectangle((snake_x, snake_y, snake_x + cell_size, snake_y + cell_size), fill=(0, 0, 0))
    if snake_direction == "right":
        snake_x += cell_size
    elif snake_direction == "down":
        snake_y += cell_size
    elif snake_direction == "left":
        snake_x -= cell_size
    elif snake_direction == "up":
        snake_y -= cell_size

# Desenhar os commits
if isinstance(commits, list):
    for commit in commits:
        if isinstance(commit, dict) and 'sha' in commit:
            commit_hash = commit['sha'][:7]
            draw.text((margin, height - margin - cell_size), commit_hash, fill=(0, 0, 0))

# Salvar a imagem como GIF
buffer = io.BytesIO()
image.save(buffer, format="GIF")

# Upload do GIF para o GitHub Actions
with open("snake.gif", "wb") as f:
    f.write(buffer.getvalue())
