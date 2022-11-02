import toml


def read_toml(filename: str):
    data = None
    with open(filename, 'r') as f:
        data = f.read()
        data = toml.loads(data)
    return data
