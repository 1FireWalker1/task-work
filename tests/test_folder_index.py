from src.scripts.update_index import main

from pathlib import Path 

def test_mix_of_known_and_unknown():
    main(Path('tests/cases/artist_and_wo_artist'))
    assert Path('tests/cases/artist_and_wo_artist').exists()
    assert Path('tests/cases/artist_and_wo_artist').is_dir()
    assert len(list(Path('tests/cases/artist_and_wo_artist').glob('*'))) == 2
    assert Path('tests/cases/artist_and_wo_artist/Blur (2)').exists()
    assert Path('tests/cases/artist_and_wo_artist/Blur (2)').is_dir()
    assert len(list(Path('tests/cases/artist_and_wo_artist/Blur (2)').glob('*'))) == 2
    assert Path('tests/cases/artist_and_wo_artist/Blur (2)/song3 [Blur].mp3').exists()
    assert Path('tests/cases/artist_and_wo_artist/Blur (2)/song3 [Blur].mp3').is_file()
    assert Path('tests/cases/artist_and_wo_artist/Blur (2)/song2 [Blur].mp3').exists()
    assert Path('tests/cases/artist_and_wo_artist/Blur (2)/song2 [Blur].mp3').is_file()
    assert Path('tests/cases/artist_and_wo_artist/VA (2)').is_dir()
    assert Path('tests/cases/artist_and_wo_artist/VA (2)').exists()
    assert len(list(Path('tests/cases/artist_and_wo_artist/VA (2)').glob('*'))) == 2
    assert Path('tests/cases/artist_and_wo_artist/VA (2)/unknown.mp3').exists()
    assert Path('tests/cases/artist_and_wo_artist/VA (2)/unknown.mp3').is_file()
    assert Path('tests/cases/artist_and_wo_artist/VA (2)/unknown2.mp3').exists()
    assert Path('tests/cases/artist_and_wo_artist/VA (2)/unknown2.mp3').is_file()

def test_empty_dir():
    Path('tests/cases/empty_dir').mkdir(parents=True, exist_ok=True)
    main(Path('tests/cases/empty_dir'))
    assert Path('tests/cases/empty_dir').exists()
    assert Path('tests/cases/empty_dir').is_dir()
    assert len(list(Path('tests/cases/empty_dir').glob('*'))) == 0


def test_folder_with_tracks_other_wo():
    main(Path('tests/cases/folder_with_tracks_other_wo'))
    assert Path('tests/cases/folder_with_tracks_other_wo').exists()
    assert Path('tests/cases/folder_with_tracks_other_wo').is_dir()
    assert len(list(Path('tests/cases/folder_with_tracks_other_wo').glob('*'))) == 2

    assert Path('tests/cases/folder_with_tracks_other_wo/empty (0)').exists()
    assert Path('tests/cases/folder_with_tracks_other_wo/empty (0)').is_dir()
    assert len(list(Path('tests/cases/folder_with_tracks_other_wo/empty (0)').glob('*'))) == 0

    assert Path('tests/cases/folder_with_tracks_other_wo/VA (1)').is_dir()
    assert Path('tests/cases/folder_with_tracks_other_wo/VA (1)').exists()
    assert len(list(Path('tests/cases/folder_with_tracks_other_wo/VA (1)').glob('*'))) == 1
    assert Path('tests/cases/folder_with_tracks_other_wo/VA (1)/1.mp3').exists()
    assert Path('tests/cases/folder_with_tracks_other_wo/VA (1)/1.mp3').is_file()


def test_artist_reg_sense_few_words():
    main(Path('tests/cases/artist_reg_sense_few_words'))
    assert Path('tests/cases/artist_reg_sense_few_words').exists()
    assert Path('tests/cases/artist_reg_sense_few_words').is_dir()
    assert len(list(Path('tests/cases/artist_reg_sense_few_words').glob('*'))) == 1

    assert Path('tests/cases/artist_reg_sense_few_words/Imagine Dragons (3)').exists()
    assert Path('tests/cases/artist_reg_sense_few_words/Imagine Dragons (3)').is_dir()
    assert len(list(Path('tests/cases/artist_reg_sense_few_words/Imagine Dragons (3)').glob('*'))) == 3

    assert Path('tests/cases/artist_reg_sense_few_words/Imagine Dragons (3)/demons [Imagine Dragons].mp3').exists()
    assert Path('tests/cases/artist_reg_sense_few_words/Imagine Dragons (3)/demons [Imagine Dragons].mp3').exists()

    assert Path('tests/cases/artist_reg_sense_few_words/Imagine Dragons (3)/radioactive [Imagine Dragons].mp3').exists()
    assert Path('tests/cases/artist_reg_sense_few_words/Imagine Dragons (3)/radioactive [Imagine Dragons].mp3').is_file()
    
    assert Path('tests/cases/artist_reg_sense_few_words/Imagine Dragons (3)/Thunder [Imagine Dragons].mp3').is_file()
    assert Path('tests/cases/artist_reg_sense_few_words/Imagine Dragons (3)/Thunder [Imagine Dragons].mp3').is_file()
    
    

def test_two_artist_in_branches():
    try:
        main(Path('tests/cases/two_artist_in_branches'))
        assert False, 'ожидали ошибку'
    
    except ValueError:
        ...

def test_file_in_root():
    try:
        main(Path('tests/cases/file_in_root'))
        assert False, 'ожидали ошибку'
        
    except ValueError:
        ...
        
def test_sub_folder():
    try:
        main(Path('tests/cases/sub_folder'))
        assert False, 'ожидали ошибку'
        
    except ValueError:
        ...

def test_unknown_root_path():
    try:
        main(Path('tests/cases/unknown_path'))
        assert False, 'ожидали ошибку'

    except FileNotFoundError:
        ...


def test_wrong_type():
    try:
        main('tests/cases/empty_dir')
        assert False, 'ожидали ошибку'

    except AttributeError:
        ...

    
