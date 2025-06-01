from pathlib import Path
from src.media_indexing.folder_index import get_artist, remove_artist, remove_counter, Media, Folder

import pytest

def test_get_artist_one_artist():
   assert get_artist("pin the grenade [Blink 182].mp3") == "Blink 182"


def test_get_no_artist():
   assert get_artist('unknown song.mp3') == None

def test_get_two_artist():
    try:
        get_artist('broken [One][Two].mp3')
        pytest.fail()

    except Exception:
        return


def test_remove_artist_exist():
    assert remove_artist("pin the grenade [Blink 182].mp3") == 'pin the grenade .mp3'

def test_remove_artist_not_exist():
    assert remove_artist("pin the grenade.mp3") == 'pin the grenade.mp3'

def test_remove_counter():
    assert remove_counter('Blink 182 (3)') == 'Blink 182'

def test_remove_counter_not_exist():
    assert remove_counter('Blink 182') == 'Blink 182'

def test_media_is_dir():
    try:
        Media('tests')
        pytest.fail()

    except Exception:
        return

def test_media_is_file():
    got = Media(Path('pyproject.toml'))
    assert got.artist_name == None
    assert got.path == Path('pyproject.toml')
    assert got.title == 'pyproject'

def test_media_rename_update():
    with Path('temp [artist].mp3').open(mode='w') as f:
        ...

    obj = Media(Path('temp [artist].mp3'))
    obj.rename_update()
    assert obj.artist_name == 'Artist'
    assert obj.title == 'temp'
    assert obj.path == Path('temp [Artist].mp3')

def test_folder():
    got = Folder(Path('tests'))
    assert got.path == Path('tests')
    assert got.title == 'tests'

def test_folder_not_folder():
    try:
        got = Folder(Path('pyproject.toml'))
        pytest.fail()
    
    except Exception:
        return