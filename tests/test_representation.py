from versionify import Version

class TestRepresentation:
    def test_representation_str(self):
        assert str(Version.parse('1.2.3')) == '1.2.3'
        assert str(Version.parse('1.0.0-alpha')) == '1.0.0-alpha'
        assert str(Version.parse('1.0.0+build.1')) == '1.0.0+build.1'
        assert str(Version.parse('1.0.0-alpha+build.1')) == '1.0.0-alpha+build.1'

    def test_representation_repr(self):
        assert repr(Version.parse('1.2.3')) == "Version('1.2.3')"
        assert repr(Version.parse('1.0.0-alpha')) == "Version('1.0.0-alpha')"
        assert repr(Version.parse('1.0.0+build.1')) == "Version('1.0.0+build.1')"
        assert repr(Version.parse('1.0.0-alpha+build.1')) == "Version('1.0.0-alpha+build.1')"
