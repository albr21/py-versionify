from versionify import Version

class TestBump:
    def test_bump_major(self):
        assert str(Version.parse('1.2.3').bump_major()) == '2.0.0'

    def test_bump_minor(self):
        assert str(Version.parse('1.2.3').bump_minor()) == '1.3.0'

    def test_bump_patch(self):
        assert str(Version.parse('1.2.3').bump_patch()) == '1.2.4'
