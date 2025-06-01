import os
import shutil
from typing import Generator

from src.scripts.update_index import *
import pytest



def check_directory_structure(expected_tree: dict, root_dir: str):
    current_elements = set(os.listdir(root_dir))

    for name, content in expected_tree.items():
        if name not in current_elements:
            return False
        
        full_path = os.path.join(root_dir, name)
        
        if content is None:
            if not os.path.isfile(full_path):
                print(f'{full_path} должно быть файлом')
                return False
            
        else:
            if not os.path.isdir(full_path):
                return False
                
            if not check_directory_structure(content, full_path):
                return False
    
    unexpected_elements = current_elements - set(expected_tree.keys())
    if unexpected_elements:
        return False
    
    return True

@pytest.fixture
def temp_dir() -> Generator[Path]:
    path = Path('test_data')

    if path.exists():
        shutil.rmtree(path=path)

    path.mkdir(parents=True, exist_ok=True)

    yield path

    if path.exists():
        shutil.rmtree(path=path)


def test_couple_artists_and_unknown(temp_dir: Path):
    goat = temp_dir / 'goat'
    goat.mkdir(parents=True, exist_ok=True)
    
    with (goat / 'highway to hell [Ac Dc].mp3').open(mode='w') as f:
        ...
    
    with (goat / 'Eye of the tiger [survivor].mp3').open(mode='w') as f:
        ...

    with (goat / 'Back to black [Ac dc].mp3').open(mode='w') as f:
        ...

    with (goat / 'untitled.mp3').open(mode='w') as f:
        ...

    second_places = temp_dir / 'second_places'
    second_places.mkdir(parents=True, exist_ok=True)
    with (second_places / 'Bohemian rapsody [Queen].mp3').open(mode='w') as f:
        ...

    with (second_places / 'cool_rock.mp3').open(mode='w') as f:
        ...

    with (second_places / 'unknown_artist_2.mp3').open(mode='w') as f:
        ...

    main(temp_dir)

    assert check_directory_structure(
        expected_tree={
            "Ac Dc (2)": {
                "Back to black [Ac Dc].mp3": None,
                "highway to hell [Ac Dc].mp3": None,
            },
            "Queen (1)": {
                "Bohemian rapsody [Queen].mp3": None,
            },
            "Survivor (1)": {
                "Eye of the tiger [Survivor].mp3": None,
            },
            "VA (3)": {
                "cool_rock.mp3": None,
                "unknown_artist_2.mp3": None,
                "untitled.mp3": None,
            }
        },
        root_dir=temp_dir,
    )



