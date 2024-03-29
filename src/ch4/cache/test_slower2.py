import pytest
from collections import namedtuple
import datetime

Duration = namedtuple('Duration', ['current', 'last'])

@pytest.fixture(scope='session')
def duration_cache(request):
    key ='duration/testdurations'
    d = Duration({}, request.config.cache.get(key, {}))
    yield d
    request.config.cache.set(key, d.current)


@pytest.fixture(autouse=True)
def check_duration(request, duration_cache):
    d = duration_cache
    nodeid = request.node.nodeid
    start_time = datetime.datetime.now()
    yield
    duration = (datetime.datetime.now() - start_time).total_seconds()
    d.current[nodeid] = duration
    if d.lastget(nodeid, None) is not None:
        errorstring = "test duration over 2x last duration"
        assert duration <= (d.last[nodeid] * 2), errorstring
