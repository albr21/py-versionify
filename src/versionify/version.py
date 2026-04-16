from functools import total_ordering
from .parser import parse as _parse
from .bump import bump_major, bump_minor, bump_patch

@total_ordering
class Version:
    def __init__(self, major: int, minor: int, patch: int, prerelease: str = None, buildmetadata: str = None) -> None:
        self.major = major
        self.minor = minor
        self.patch = patch
        self.prerelease = prerelease
        self.buildmetadata = buildmetadata

    @classmethod
    def parse(cls, value: str) -> "Version":
        parts = _parse(value)
        return cls(**parts)

    def __str__(self) -> str:
        base = f"{self.major}.{self.minor}.{self.patch}"
        if self.prerelease:
            base += f"-{self.prerelease}"
        if self.buildmetadata:
            base += f"+{self.buildmetadata}"
        return base

    def __repr__(self) -> str:
        return f"Version('{self}')"

    def _cmp_key(self) -> tuple:
        return (
            self.major,
            self.minor,
            self.patch,
            self.__prerelease_key(),
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Version):
            raise TypeError(f"Cannot compare Version with {type(other)}")
        return self._cmp_key() == other._cmp_key()

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Version):
            raise TypeError(f"Cannot compare Version with {type(other)}")
        return self._cmp_key() < other._cmp_key()
    
    def __prerelease_key(self) -> tuple:
        if self.prerelease is None:
            return (1,)
        return (0, self.__split_prerelease(self.prerelease))
    
    def __split_prerelease(self, prerelease: str) -> tuple:
        parts = []
        for ident in prerelease.split("."):
            if ident.isdigit():
                parts.append((0, int(ident)))
            else:
                parts.append((1, ident))
        return tuple(parts)

    def bump_major(self) -> "Version":
        return Version(*bump_major(self))

    def bump_minor(self) -> "Version":
        return Version(*bump_minor(self))

    def bump_patch(self) -> "Version":
        return Version(*bump_patch(self))
