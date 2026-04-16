# py-versionify

A Python module to manage versions following [semver](https://semver.org/).

## Usage

```python
from versionify import Version

version = Version("1.0.0")
version = version.bump_major()
version = version.bump_minor()
version = version.bump_patch()

print(version)
# Output: 2.1.1

# Comparisons
Version("1.0.0") < Version("2.0.0")
```

## Contributing

Check out the [CONTRIBUTING](CONTRIBUTING.md) file for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
