import pytest
from pathlib import Path
from src.media_indexing.folder_index import Media

@pytest.fixture
def test_media(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "test.mp3"
    p.write_text("")
    m = Media(p)
    return m

def test_init(test_media):
    assert isinstance(test_media.path, Path)
    assert test_media.artist_name is None
    assert test_media.title == "test"

def test_rename_update(test_media):
    test_media.artist_name = "Test Artist"
    test_media.rename_update()
    assert test_media.path.name == "test [Test Artist].mp3"