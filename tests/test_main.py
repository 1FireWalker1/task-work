import pytest
from src.scripts.update_index import main

@pytest.fixture
def temp_input_dir(tmp_path):
    input_dir = tmp_path / "input"
    input_dir.mkdir()
    sub1 = input_dir / "sub1"
    sub1.mkdir()
    p1 = sub1 / "track1.mp3"
    p1.write_text("")
    sub2 = input_dir / "sub2"
    sub2.mkdir()
    p2 = sub2 / "track2.mp3"
    p2.write_text("")
    
    yield input_dir

def test_main(temp_input_dir):
    main(temp_input_dir)
    
    va_folder = temp_input_dir / "VA (2)"
    assert va_folder.exists(), "Файловые папки не созданы."
    
    files_in_va = list(va_folder.glob("*"))
    assert len(files_in_va) == 2, "Ожидалось ровно два файла в итоговом каталоге."

    track1 = va_folder / "track1.mp3"
    track2 = va_folder / "track2.mp3"
    assert track1.exists(), "Файл track1.mp3 отсутствует."
    assert track2.exists(), "Файл track2.mp3 отсутствует."
