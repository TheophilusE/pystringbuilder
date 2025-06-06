# StringBuilder

A high-performance Python string builder class designed for efficient manipulation of large text. This class implements custom, in-place algorithms to minimize costly string conversion operations and reduce heap allocations when building long strings.

## Overview

StringBuilder is a Python class that provides an efficient way to construct and modify strings while minimizing memory allocations. Unlike Python's native string operations, which can lead to frequent memory reallocations, this implementation preallocates an internal buffer to improve performance for large string manipulations.

## Features

- **Preallocated Buffer**: Manages memory with a preallocated array to minimize frequent heap allocations.
- **Fluent API**: Supports chaining of methods like `append()`, `insert()`, `delete()`, and more.
- **Comprehensive String Operations**: Includes functionality for replacing substrings, trimming whitespace (beginning, end, or both), reversing the string, and extracting substrings.
- **Iterator & Indexing Support**: Provides native Python indexing, slicing, and iteration over the characters.
- **Efficient Search**: Uses an optimized algorithm (like the Knuth-Morris-Pratt algorithm) for substring search in large texts.

## Installation

To use StringBuilder in your project:
1. Download the `stringbuilder.py` file containing the implementation.
2. Place the file in your project directory.
3. Import it as needed using:
   ```python
   from stringbuilder import StringBuilder
   ```

A PyPI package may be published at a later date.

This class requires only a standard Python 3.x environment. Python 2.x might work with minor fixes.

## Basic Example
```python
from stringbuilder import StringBuilder

# Initialize with default capacity.
sb = StringBuilder()

# Append text and then append a line break.
sb.append("Hello").append(", ").append_line("World!")

# Insert additional text.
sb.insert(7, "Beautiful ")

# Delete a segment of text.
sb.delete(7, 17)

# Replace a substring.
sb.replace("World", "Universe")

# Trim extraneous whitespace.
sb.append("   Extra text   ")
sb.trim()  # Removes both leading and trailing whitespace.

# Get a substring and reverse the content.
substring = sb.substring(0, 5)
sb.reverse()

# Use syntactic sugar for addition.
sb += " More text"
sb_new = sb + " Even more text"

# Print resulting string.
print(str(sb))
```

## API Documentation
### Initialization
* `StringBuilder(iCapacity: int = 1024)` Initializes the StringBuilder with an optional preallocated capacity.

### Core Methods
* `append(szText)`: Appends a string (or any object convertible to a string) to the builder and returns the updated StringBuilder instance.
* `append_line(szText: str = "")`: Appends the provided text followed by a newline character.
* `insert(iIndex: int, szText: str)`: Inserts text at the specified index. Raises `IndexError` if the index is out of bounds.
* `delete(iStart: int, iEnd: int)`: Removes characters in the range [iStart, iEnd). Raises `IndexError` for invalid indices.
* `replace(szOld: str, szNew: str)`: Replaces all occurrences of the substring `szOld` with `szNew`. Depending on the size and patterns involved, it adjusts the internal buffer accordingly.
* `clear()`: Clears the current content inside the builder.
* `reverse()`: Reverses the entire string content in-place.
* `trim()`, `trim_start()`, `trim_end()`: Removes whitespace from both ends, the start, or the end of the string, respectively.
* `substring(iStart: int, iEnd: int = None)`: Returns a substring from the specified starting index up to (but not including) the ending index. If iEnd is omitted, it returns until the end of the string.
* `find(szSub: str, iStart: int = 0, iEnd: int = None)`: Searches for the first occurrence of szSub in the string between the indices iStart and iEnd.

### Operator Overloads
* `__str__()`: Returns the built string.
* `__repr__()`: Provides a formal string representation of the StringBuilder instance.
* `__len__()`: Returns the current length of the built content.
* `__iadd__(szOther)`: Overloads the `+=` operator to append text.
* `__add__(szOther)`: Overloads the `+` operator to produce a new StringBuilder instance with concatenated content.
* `__getitem__(key)`: Allows indexing and slicing of the builder's content.
* `__iter__()`: Enables iteration over the characters of the built string.

## Unit Tests
Unit tests for the StringBuilder class are provided in the stringbuildertest.py file. To run the tests, execute:

```bash
python -m unittest ./tests/stringbuildertest.py
```

## Contributing

Contributions, improvements, and bug fixes are welcome! Please follow the existing coding style and include unit tests for new features or fixes.

## License

This project is licensed under the MIT License.
