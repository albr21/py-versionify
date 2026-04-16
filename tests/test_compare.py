import pytest
from versionify import Version

class TestCompare:
    def test_compare_release_greater_than_prerelease(self):
        assert Version.parse('1.0.0-alpha') < Version.parse('1.0.0')

    def test_compare_prerelease_order(self):
        assert Version.parse('1.0.0-alpha') < Version.parse('1.0.0-alpha.1')
        assert Version.parse('1.0.0-alpha.1') < Version.parse('1.0.0-alpha.beta')
        assert Version.parse('1.0.0-beta') < Version.parse('1.0.0-beta.2')
        assert Version.parse('1.0.0-beta.2') < Version.parse('1.0.0-beta.11')
        assert Version.parse('1.0.0-rc.1') < Version.parse('1.0.0')

    def test_compare_buildmetadata_ignored_in_comparison(self):
        assert Version.parse('1.0.0+build.1') == Version.parse('1.0.0+build.2')
        assert Version.parse('1.0.0-alpha+build.1') == Version.parse('1.0.0-alpha+build.2')

    def test_compare_major_minor_patch_comparison(self):
        assert Version.parse('1.0.0') < Version.parse('2.0.0')
        assert Version.parse('1.0.0') < Version.parse('1.1.0')
        assert Version.parse('1.0.0') < Version.parse('1.0.1')
        assert Version.parse('1.2.3') < Version.parse('1.2.4')
        assert Version.parse('1.2.3') < Version.parse('1.3.0')
        assert Version.parse('1.2.3') < Version.parse('2.0.0')

    def test_compare_equality(self):
        assert Version.parse('1.0.0') == Version.parse('1.0.0')
        assert Version.parse('1.0.0-alpha') == Version.parse('1.0.0-alpha')
        assert Version.parse('1.0.0+build.1') == Version.parse('1.0.0+build.1')
        assert Version.parse('1.0.0+build.1') == Version.parse('1.0.0+build.2')
        assert Version.parse('1.0.0-alpha+build.1') == Version.parse('1.0.0-alpha+build.1')
        assert Version.parse('1.0.0-alpha+build.1') == Version.parse('1.0.0-alpha+build.2')

    def test_compare_inequality(self):
        assert Version.parse('1.0.0') != Version.parse('1.0.1')
        assert Version.parse('1.0.0-alpha') != Version.parse('1.0.0-beta')

    def test_compare_invalid_comparison(self):
        with pytest.raises(TypeError):
            Version.parse('1.0.0') < "1.0.0"
        with pytest.raises(TypeError):
            Version.parse('1.0.0') == "1.0.0"

    def test_compare_full_comparison(self):
        assert Version.parse('1.0.0-alpha') < Version.parse('1.0.0-alpha.1') < Version.parse('1.0.0-alpha.beta') < Version.parse('1.0.0-beta') < Version.parse('1.0.0-beta.2') < Version.parse('1.0.0-beta.11') < Version.parse('1.0.0-rc.1') < Version.parse('1.0.0')

    def test_compare_gt_and_lt(self):
        assert Version.parse('1.0.0') > Version.parse('1.0.0-alpha')
        assert Version.parse('1.0.0') >= Version.parse('1.0.0')
        assert Version.parse('1.0.0') <= Version.parse('1.0.0')
        assert Version.parse('1.0.0-alpha') <= Version.parse('1.0.0')
        assert Version.parse('1.0.0-alpha') >= Version.parse('1.0.0-alpha')
        assert Version.parse('1.0.0-alpha') < Version.parse('1.0.0')
