# advent-of-code-2023

[![PyPI - Version](https://img.shields.io/pypi/v/advent-of-code-2023.svg)](https://pypi.org/project/advent-of-code-2023)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/advent-of-code-2023.svg)](https://pypi.org/project/advent-of-code-2023)

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Tips for the CLI-inclined player

### Save prompt as GFM
Download today's prompt,
and translate it on the flight into
[GitHub Flavored Markdown](https://github.github.com/gfm/)
(or any format you prefer) using 
[curl](https://curl.se)+[pandoc](https://pandoc.org) :

    curl https://adventofcode.com/<year>/day/<day> | pandoc -f html -t gfm -o <destination>

### Download the input file
In order to download the input file,
since it is different for each user,
you need to provide your session cookie!
Locate and save AoC's session cookie using your browser.
Append it to curl using:

    curl --cookie "session=${AOC_SESSION_COOKIE}" https://adventofcode.com/<year>/day/<3>/input -o <destination-path>


## License

`advent-of-code-2023` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
