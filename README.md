# Difference Calculator
installation:
1. Clone this repo
2. Open console in directory with the clone repo
3. If poetry doesn't installed `pip install poetry`
<br>3.1. Run `poetry install` 
4. Create a build `make build`
5. Public code `make public`
6. Install `make package-install`

### Hexlet tests and linter status:
[![Actions Status](https://github.com/Timo4ey/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/Timo4ey/python-project-50/actions)

### My Github Actions Test
[![Tests Status](https://github.com/Timo4ey/python-project-50/actions/workflows/genndiff.yml/badge.svg)](https://github.com/Timo4ey/python-project-50/actions/workflows/genndiff.yml)

### Maintainability Badge
[![Maintainability](https://api.codeclimate.com/v1/badges/359f6c5da096b7b6cc8c/maintainability)](https://codeclimate.com/github/Timo4ey/python-project-50/maintainability)

### Test Coverage Badge
[![Test Coverage](https://api.codeclimate.com/v1/badges/359f6c5da096b7b6cc8c/test_coverage)](https://codeclimate.com/github/Timo4ey/python-project-50/test_coverage)

### Flat File Comparison (JSON)
Command: ```gendiff test_1_file1.json test_1_file2.json```

[![asciicast](https://asciinema.org/a/TAGMPiTfasUTgAA4t13gInJn5.svg)](https://asciinema.org/a/TAGMPiTfasUTgAA4t13gInJn5)

### Flat File Comparsion (YML)
Command: ```gendiff test_1_yaml_file1.yml test_1_yaml_file2.yml```

[![asciicast](https://asciinema.org/a/IqcVfDZptEuyGQ7ZV8HbdXX1z.svg)](https://asciinema.org/a/IqcVfDZptEuyGQ7ZV8HbdXX1z)

### Recursive files Comparison

[![asciicast](https://asciinema.org/a/mGk9IRM5wxHK12oVPMKt3jZTv.svg)](https://asciinema.org/a/mGk9IRM5wxHK12oVPMKt3jZTv)

### Plain files Comparison
Command: ```gendiff --format plain test_5_recurs_file1.json test_5_recurs_file2.json```
[![asciicast](https://asciinema.org/a/mqLIHmT6dhRGDIYrqKGIig4zh.svg)](https://asciinema.org/a/mqLIHmT6dhRGDIYrqKGIig4zh)
