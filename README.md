# Caption Processor Utility

## Overview
The Caption Processor is a command-line utility designed to process SMPTE Timecode-based captions. It reads an input file containing timecode, speaker names, and speech text, and outputs a formatted text file with the specified modifications.

## Features
- Removes all lines containing timecode.
- Consolidates speech from the same speaker into a single block.
- Formats speaker names in bold followed by a colon.

## Installation
To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Input file format
A txt file formatted as follows

```
00:00:00:00 - 00:00:22:19
Speaker 1
I'm going to tell you something very important

00:00:22:20 - 00:00:27:22
Speaker 1
but I think you'll have to a wait a while before I tell you

00:00:27:24 - 00:00:30:02
Speaker 2
This is very frustrating.
```

## Usage
To run the utility, use the following command in the terminal:

```
python src/main.py <input_file> <output_file>
```

Replace `<input_file>` with the path to your input file containing the SMPTE Timecode-based captions, and `<output_file>` with the desired path for the output file.

## Testing
To run the tests, navigate to the `tests` directory and execute:

```
pytest
```

This will run all unit tests defined in the `test_processor.py` file.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.


# To run command from anywhere
## Install pipx 
```
brew install pipx
pipx ensurepath
```

## Install this package
```
cd /Users/gpanciera/caea/video-interview-parser/caption-processor
pipx install .
```