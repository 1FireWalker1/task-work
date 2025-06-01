import pytest
from pathlib import Path
from src.media_indexing.folder_index import get_updated_media_paths, apply_new_media_paths, reindex_folders, get_folders

@pytest.fixture
def test_base_dir(tmp_path):
    d = tmp_path / "base"
    d.mkdir()
    sub1 = d / "sub1"
    sub1.mkdir()
    p1 = sub1 / "test1.mp3"
    p1.write_text("")
    sub2 = d / "sub2"
    sub2.mkdir()
    p2 = sub2 / "test2.mp3"
    p2.write_text("")
    return d

def test_get_updated_media_paths(test_base_dir):
    updated_paths = get_updated_media_paths(test_base_dir)
    assert len(updated_paths) == 2
    assert all(isinstance(k, Path) and isinstance(v, Path) for k, v in updated_paths.items())

def test_apply_new_media_paths(test_base_dir):
    updated_paths = get_updated_media_paths(test_base_dir)
    apply_new_media_paths(updated_paths)
    assert len(list(test_base_dir.glob("*"))) == 1
    assert len(list((test_base_dir / "VA").glob("*"))) == 2

def test_reindex_folders(test_base_dir):
    folders = get_folders(test_base_dir)
    reindex_folders(folders)
    assert len(list(test_base_dir.glob("*"))) == 2
    assert len(list((test_base_dir / "sub1 (1)").glob("*"))) == 1
    assert len(list((test_base_dir / "sub2 (1)").glob("*"))) == 1