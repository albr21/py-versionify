def bump_major(version):
    return (
        version.major + 1,
        0,
        0,
        None,
        None,
    )

def bump_minor(version):
    return (
        version.major,
        version.minor + 1,
        0,
        None,
        None,
    )

def bump_patch(version):
    return (
        version.major,
        version.minor,
        version.patch + 1,
        None,
        None,
    )