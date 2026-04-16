import pytest
from versionify import Version
from versionify.errors import InvalidVersionError

class TestParse:
    @pytest.mark.parametrize('value', [
        '0.0.0','1.2.3','10.20.30','1.0.0-alpha','1.0.0-alpha.1','1.0.0+build.1','1.0.0-alpha+build.1'
    ])
    def test_parse_valid_parse(self, value):
        Version.parse(value)

    @pytest.mark.parametrize('value', [
        '','1','1.2','1.2.3.4','01.2.3','1.02.3','1.2.03','1.2.-3','1.2.3-','1.2.3+','v1.2.3'
    ])
    def test_parse_invalid_parse(self, value):
        with pytest.raises(InvalidVersionError):
            Version.parse(value)
