from .constants import SEMVER_REGEX
from .errors import InvalidVersionError

def parse(value: str) -> dict:
    match = SEMVER_REGEX.match(value)
    if not match:
        raise InvalidVersionError(f"Invalid semantic version: {value}")

    parts = match.groupdict()
    prerelease = parts.get("prerelease")

    return {
        "major": int(parts["major"]),
        "minor": int(parts["minor"]),
        "patch": int(parts["patch"]),
        "prerelease": prerelease,
        "buildmetadata": parts.get("buildmetadata"),
    }
