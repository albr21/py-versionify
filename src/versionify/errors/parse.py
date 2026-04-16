from .base import VersionifyError

class InvalidVersionError(VersionifyError):
    """Raised when a version string is not valid SemVer."""
