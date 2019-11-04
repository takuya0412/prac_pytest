import json


def test_brian_in_portland(author_file_json):
    with author_file_json.open() as file:
        authors = json.load(file)

    assert authors['Brian']['City'] == 'Portland'


def test_all_have_cities(author_file_json):
    with author_file_json.open() as f:
        authors = json.load(f)

    for a in authors:
        assert len(authors[a]['City']) > 0
