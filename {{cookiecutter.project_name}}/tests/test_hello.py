from {{cookiecutter.project_name}}.hello import hello


def test_hello() -> None:
    assert hello() == "hello"
