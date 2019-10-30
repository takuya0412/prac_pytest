import pytest
import tasks
from tasks import Task


@pytest.fixture()
def tasks_db(tmpdir):
    tasks.start_tasks_db(str(tmpdir), 'tiny')
    yield
    tasks.stop_tasks_db()


@pytest.fixture()
def tasks_just_a_few():
    return (
        Task('Write  some code', 'Brian', True),
        Task("Code review Brian's code", 'Katie', False),
        Task('Fix what Brian did', 'Michelle', False)
    )


@pytest.fixture()
def tasks_multi_per_owner():
    return (Task('Make a cookie', 'Raphael'),
            Task('Use an emoji', 'Raphael'),
            Task('Move to Berlin', 'Raphael'),

            Task('Create', 'Michelle'),
            Task('Inspire', 'Michelle'),
            Task('Encourage', 'Michelle'),

            Task('Do a handstand', 'Daniel'),
            Task('Write some books', 'Daniel'),
            Task('Eat ice cream', 'Daniel'))


@pytest.fixture()
def db_with_3_tasks(tasks_db, tasks_just_a_few):
    for t in tasks_just_a_few:
        tasks.add(t)


@pytest.fixture()
def db_with_multi_per_ownre(tasks_db, tasks_mult_per_owner):
    for t in tasks_mult_per_owner:
        tasks.add(t)

@pytest.fixture(scope='session')
def tasks_db_session(tmpdir_factory):
    temp_dir = tmpdir_factory.mktemp('temp')
    tasks.start_tasks_db(str(temp_dir), 'tiny')
    yield
    tasks.stop_tasks_db()


@pytest.fixture()
def tasks_db(tasks_db_session):
    tasks.delete_all()


@pytest.fixture(scope='session')
def tasks_db_session(tmpdir_factory):
    temp_dir = tmpdir_factory.mktemp('temp')
    tasks.start_tasks_db(str(temp_dir), 'tiny')
    yield
    tasks.stop_tasks_db()


@pytest.fixture()
def tasks_db(tasks_db_session):
    tasks.delete_all()


@pytest.fixture(scope='session')
def tasks_just_a_few():
    return (
        Task('Write some code', 'Brian', True),
        Task("Code review Brian's  code", 'Katie', False),
        Task("Fix what Brian did", "Michell", False),
    )

@pytest.fixture(scope='session')
def tasks_mult_per_owner():
    return (
        Task('Make a cookie', 'Raphael'),
        Task('Use an emoji', 'Raphael'),
        Task('Move to Berlin', 'Raphael'),

        Task('Create', 'Micheal'),
        Task('Inspire', 'Micheal'),
        Task('Encourage', 'Micheal'),


    )
