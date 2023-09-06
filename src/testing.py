import toml

with open("pyproject.toml", "r", encoding="UTF-8") as f:
    config = toml.load(f)
    
    print(config["tool"]["poetry"]["version"])