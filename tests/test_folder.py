import pytest
from pathlib import Path
from src.media_indexing.folder_index import Folder, Media

@pytest.fixture
def test_folder(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "test.mp3"
    p.write_text("")
    f = Folder(d)
    return f

def test_get_media_list(test_folder):
    media_list = test_folder.get_media_list()
    assert len(media_list) == 1
    assert isinstance(media_list[0], Media)

def test_get_counter(test_folder):
    counter = test_folder.get_counter()
    assert counter == 1

def test_get_new_folder_name(test_folder):
    new_name = test_folder.get_new_folder_name()
    assert new_name == "sub (1)"

def test_rename_with_counter(test_folder):
    test_folder.rename_with_counter()
    assert test_folder.path.name == "sub (1)"