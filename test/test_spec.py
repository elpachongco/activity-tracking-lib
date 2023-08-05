from desktopspy.desktopspy import trackers as t


def test_getForegroundWindow():
    """Test getForegroundWindow returns a tuple of two elements: string and int"""
    actual = t.getForegroundWindow()
    assert isinstance(actual, tuple), 'Should return a tuple'
    assert len(actual) == 2, 'Should have 2 elements'
    assert isinstance(actual[0], str), 'first item should be string'
    assert isinstance(actual[1], int) or actual[1] is None, 'second item should be int  \
        or None'


def test_isUserActive():
    """Test isUserActive returns a boolean"""
    actual = t.isUserActive()
    assert isinstance(actual, bool)
