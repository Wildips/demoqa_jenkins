from pathlib import Path


def path(file_name):
    # os.path.realpath(f'image/{file_name}')
    return str(Path(__file__).parent.joinpath(f'image/{file_name}').absolute())
