import pytest
from pathlib import Path
from src.scripts.update_index import main

def create_files(files: list[Path]):
    for file in files:
        with file.open(mode='w'):
            ...

@pytest.fixture(scope='module')
def setup_test_environment(tmp_path_factory):
    root_dir = tmp_path_factory.mktemp("music_collection")
    chills_dir = root_dir / "Chill Vibes"
    classic_hits_dir = root_dir / "Classic Hits"
    mixed_genres_dir = root_dir / "Mixed Genres"
    empty_dir = root_dir / "Empty Folder"
    special_chars_dir = root_dir / "Special Characters"
    broken_data_dir = root_dir / "Broken Data"
    chills_dir.mkdir()
    classic_hits_dir.mkdir()
    mixed_genres_dir.mkdir()
    empty_dir.mkdir()
    special_chars_dir.mkdir()
    broken_data_dir.mkdir()
    
    create_files(
        [
            chills_dir / "song1.mp3",
            classic_hits_dir / "track1 [Artist X].mp3",
            mixed_genres_dir / "track1 [Artist Y].mp3",
            broken_data_dir / "song1 [[Artist W]].mp3",
            empty_dir / ".hidden_file",
            special_chars_dir / "song1 [Lil Pump feat. Cardi B].mp3",
        ]
    )

    yield root_dir

def test_no_artists(setup_test_environment):
    main(setup_test_environment)
    va_folder = setup_test_environment / "VA (1)"
    assert va_folder.exists()
    assert len(list(va_folder.glob("*"))) == 1

def test_one_artist(setup_test_environment):
    main(setup_test_environment)
    artist_x_folder = setup_test_environment / "Artist X (1)"
    assert artist_x_folder.exists()
    assert len(list(artist_x_folder.glob("*"))) == 1

def test_mixed_scenario(setup_test_environment):
    main(setup_test_environment)
    va_folder = setup_test_environment / "VA (1)"
    artist_y_folder = setup_test_environment / "Artist Y (1)"
    assert va_folder.exists()
    assert artist_y_folder.exists()
    assert len(list(va_folder.glob("*"))) >= 1
    assert len(list(artist_y_folder.glob("*"))) == 1

def test_empty_folder(setup_test_environment):
    main(setup_test_environment)
    empty_folder = setup_test_environment / "Empty Folder"
    assert not empty_folder.exists()

def test_special_characters(setup_test_environment):
    main(setup_test_environment)
    lil_pump_folder = setup_test_environment / "Lil Pump Feat. Cardi B (1)"
    assert lil_pump_folder.exists()
    assert len(list(lil_pump_folder.glob("*"))) == 1

def test_broken_data(setup_test_environment):
    main(setup_test_environment)
    va_folder = setup_test_environment / "VA (1)"
    assert va_folder.exists()
    assert len(list(va_folder.glob("*"))) == 1