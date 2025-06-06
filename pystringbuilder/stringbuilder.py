# MIT License
#
# Copyright (c) 2025 Theophilus Eriata <theophiluse@xiitechnologies.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

class StringBuilder:
    """
    A Python string builder class which uses an internal preallocated buffer
    to reduce the number of heap allocations. When the internal buffer is
    exceeded, it resizes to accommodate the extra text.

    Note: Though the design mimics stack allocation benefits, Python always
    manages objects on the heap. The idea is to reduce the frequency of
    memory reallocations when building long strings.
    """

    def __init__(self, iCapacity: int = 1024):
        """
        Initialize the string builder with a given capacity.

        :param iCapacity: Initial number of characters to preallocate.
        """
        self.iCapacity = iCapacity
        self.szBuffer  = [''] * iCapacity # Preallocate the buffer.
        self.iLength   = 0

    def _ensure_capacity(self, iAdditional: int):
        """
        Ensure the internal buffer has enough capacity to add additional characters.
        If not, the capacity is doubled or increased to fit the new size.

        :param additional: Number of additional characters that will be added.
        """
        iRequired = self.iLength + iAdditional
        if iRequired > self.iCapacity:
            iNewCapacity = max(self.iCapacity * 2, iRequired)
            szNewBuffer  = [''] * iNewCapacity

            # Copy existing content.
            szNewBuffer[0:self.iLength] = self.szBuffer[0:self.iLength]
            self.szBuffer               = szNewBuffer
            self.iCapacity              = iNewCapacity

    def append(self, szText) -> "StringBuilder":
        """
        Append a string (or any object convertible to a string) to the builder.

        :param szText: The string to append.
        :return: Self, to allow chaining.
        """
        szStr = str(szText)
        iSize = len(szStr)

        self._ensure_capacity(iSize)

        # Use slice assignment to insert characters into the preallocated space.
        self.szBuffer[self.iLength:self.iLength + iSize] = list(szStr)
        self.iLength                                    += iSize
        return self

    def append_line(self, szText: str = "") -> "StringBuilder":
        """
        Append a string followed by a newline.

        :param szText: The string to append before the newline.
        :return: Self, to allow chaining.
        """
        self.append(szText).append('\n')
        return self

    def insert(self, iIndex: int, szText: str) -> "StringBuilder":
        """
        Insert text at a given index.

        :param iIndex: Position at which to insert.
        :param szText: The text to insert.
        :return: Self, to allow chaining.
        :raises IndexError: If the index is out of bounds.
        """
        if iIndex < 0 or iIndex > self.iLength:
            raise IndexError("Index out of range.")

        szStr = str(szText)
        iSize = len(szStr)

        self._ensure_capacity(iSize)

        # Shift existing characters to the right.
        for i in range(self.iLength - 1, iIndex - 1, -1):
            self.szBuffer[i + iSize] = self.szBuffer[i]

        # Insert the new text.
        self.szBuffer[iIndex:iIndex + iSize] = list(szStr)
        self.iLength                        += iSize
        return self

    def delete(self, iStart: int, iEnd: int) -> "StringBuilder":
        """
        Delete a range of characters from start (inclusive) to end (exclusive).

        :param iStart: Starting index for deletion.
        :param iEnd: Ending index (exclusive).
        :return: Self, to allow chaining.
        :raises IndexError: If the indices are invalid.
        """
        if iStart < 0 or iEnd > self.iLength or iStart > iEnd:
            raise IndexError("Invalid start or end for deletion")

        iSize = iEnd - iStart

        # Shift characters left to overwrite the deleted segment.
        for i in range(iEnd, self.iLength):
            self.szBuffer[i - iSize] = self.szBuffer[i]

        self.iLength -= iSize
        return self

    def replace(self, szOld: str, szNew: str) -> "StringBuilder":
        """
        Replace all occurrences of a substring with a new substring.
        This implementation converts the current builder to a string, performs
        the replace, and reinitializes the builder.

        :param szOld: The substring to replace.
        :param szNew: The replacement substring.
        :return: Self, with replaced content.
        """
        # Define thresholds based on empirical testing.
        STRING_THRESHOLD  = 1000  # characters
        PATTERN_THRESHOLD = 5     # characters

        # Calculate total size.
        uiTotalSize = len(self.szBuffer) + len(szOld) + len(szNew)

        # Choose method based on size and pattern length.
        if uiTotalSize < STRING_THRESHOLD and len(szOld) < PATTERN_THRESHOLD:
            # Convert current content, do the replace, and rebuild.
            szReplaced     = str(self).replace(szOld, szNew)
            # Optionally, adjust capacity if needed.
            self.iCapacity = max(self.iCapacity, len(szReplaced))
            self.szBuffer  = [''] * self.iCapacity
            self.iLength   = 0
            self.append(szReplaced)

        else:
            if szOld == "":
                return self

            oldChars = list(szOld)
            newChars = list(szNew)
            uiOldLen = len(oldChars)
            result   = []  # Build the result as a list of characters.
            i        = 0

            while i < self.iLength:
                match = True
                # Check for a match with szOld starting at position i.
                if i <= self.iLength - uiOldLen:
                    for j in range(uiOldLen):
                        if self.szBuffer[i + j] != oldChars[j]:
                            match = False
                            break
                    if match:
                        result.extend(newChars)
                        i += uiOldLen
                        continue  # Skip the replaced segment.
                # If no match, simply append the current character.
                result.append(self.szBuffer[i])
                i += 1

            uiNewLength = len(result)
            if uiNewLength > self.iCapacity:
                self.iCapacity = uiNewLength
                self.szBuffer  = [''] * self.iCapacity

            # Copy the result back into the buffer.
            self.szBuffer[:uiNewLength] = result
            self.iLength                = uiNewLength
        return self

    def clear(self) -> None:
        """
        Clear the builder's content.
        """
        self.iLength = 0

    def reverse(self) -> "StringBuilder":
        """
        Reverse the characters in the builder in place.

        :return: Self, with reversed content.
        """
        iLeft  = 0
        iRight = self.iLength - 1
        while iLeft < iRight:
            self.szBuffer[iLeft], self.szBuffer[iRight] = self.szBuffer[iRight], self.szBuffer[iLeft]
            iLeft                                      += 1
            iRight                                     -= 1
        return self

    def trim(self) -> "StringBuilder":
        """
        Removes leading and trailing whitespace.
        """
        STRING_THRESHOLD = 1000

        if self.iLength < STRING_THRESHOLD:
            szTrimmed = str(self).strip()
            self.clear()
            self.append(szTrimmed)

        else:
            uiStart = 0
            while uiStart < self.iLength and self.szBuffer[uiStart].isspace():
                uiStart += 1

            if uiStart == self.iLength:
                # If all characters are whitespace, clear the builder.
                self.iLength = 0
                return self

            uiEnd = self.iLength - 1
            while uiEnd >= uiStart and self.szBuffer[uiEnd].isspace():
                uiEnd -= 1

            uiNewLength = uiEnd - uiStart + 1

            # If necessary, shift the trimmed content to the beginning.
            self.szBuffer[:uiNewLength] = self.szBuffer[uiStart : uiStart + uiNewLength]
            self.iLength                = uiNewLength

        return self

    def trim_start(self) -> "StringBuilder":
        """
        Removes leading whitespace.
        """
        STRING_THRESHOLD = 1000

        if self.iLength < STRING_THRESHOLD:
            szTrimmed = str(self).lstrip()
            self.clear()
            self.append(szTrimmed)

        else:
            uiStart = 0
            while uiStart < self.iLength and self.szBuffer[uiStart].isspace():
                uiStart += 1

            if uiStart > 0:
                uiNewLength                 = self.iLength - uiStart
                self.szBuffer[:uiNewLength] = self.szBuffer[uiStart:self.iLength]
                self.iLength                = uiNewLength

        return self

    def trim_end(self) -> "StringBuilder":
        """
        Removes trailing whitespace.
        """
        STRING_THRESHOLD = 1000

        if self.iLength < STRING_THRESHOLD:
            szTrimmed = str(self).rstrip()
            self.clear()
            self.append(szTrimmed)

        else:
            if self.iLength == 0:
                return self
            uiEnd = self.iLength - 1
            while uiEnd >= 0 and self.szBuffer[uiEnd].isspace():
                uiEnd -= 1
            self.iLength = uiEnd + 1

        return self

    def substring(self, iStart: int, iEnd: int = None) -> str:
        """
        Get a substring of the builder's content.

        :param iStart: Starting index.
        :param iEnd: Ending index (exclusive). If omitted, goes to the end.
        :return: The substring.
        """
        if iEnd is None:
            iEnd = self.iLength
        return ''.join(self.szBuffer[iStart:iEnd])


    @staticmethod
    def _kmp_prefix(pattern: list) -> list:
        """
        Build the longest prefix-suffix (lps) table used by the KMP algorithm.
        """
        m        = len(pattern)
        lps      = [0] * m
        uiLength = 0
        i = 1
        while i < m:
            if pattern[i] == pattern[uiLength]:
                uiLength += 1
                lps[i]    = uiLength
                i        += 1
            else:
                if uiLength:
                    uiLength = lps[uiLength - 1]
                else:
                    lps[i] = 0
                    i     += 1
        return lps

    def find(self, szSub: str, iStart: int = 0, iEnd: int = None) -> int:
        """
        Find the first occurrence of a substring within the builder.

        :param szSub: The substring to search for.
        :param iStart: Starting index for the search.
        :param iEnd: Ending index for the search; defaults to current length.
        :return: The index of the substring or -1 if not found.
        """
        STRING_THRESHOLD = 1000

        if self.iLength < STRING_THRESHOLD:
            szFullStr = str(self)
            return szFullStr.find(szSub, iStart, iEnd if iEnd is not None else self.iLength)

        else:
            if iEnd is None or iEnd > self.iLength:
                iEnd = self.iLength

            subList     = list(szSub)
            uiSubLength = len(subList)

            if uiSubLength == 0:
                return iStart

            lps = StringBuilder._kmp_prefix(subList)
            i   = iStart
            j   = 0
            while i < iEnd:
                if self.szBuffer[i] == subList[j]:
                    i += 1
                    j += 1
                    if j == uiSubLength:
                        return i - j
                else:
                    if j:
                        j = lps[j - 1]
                    else:
                        i += 1
        return -1

    def __str__(self) -> str:
        """
        Return the built string.
        """
        return ''.join(self.szBuffer[:self.iLength])

    def __repr__(self) -> str:
        """
        Return a formal string representation.
        """
        return f"StringBuilder({str(self)})"

    def __len__(self) -> int:
        """
        Return the current length of the built content.
        """
        return self.iLength

    def __iadd__(self, szOther) -> "StringBuilder":
        """
        Overload the '+=' operator to append text.
        """
        return self.append(szOther)

    def __add__(self, szOther) -> "StringBuilder":
        """
        Overload the '+' operator to concatenate and return a new StringBuilder.
        """
        sbNew = StringBuilder(self.iLength + len(str(szOther)))
        sbNew.append(str(self))
        sbNew.append(szOther)
        return sbNew

    def __getitem__(self, key):
        """
        Allow indexing and slicing of the builder's content.

        :param key: An index or slice.
        :return: A single character (if index) or a substring (if slice).
        :raises IndexError: if the index is out of range.
        """
        if isinstance(key, slice):
            return ''.join(self.szBuffer[:self.iLength])[key]
        elif isinstance(key, int):
            if key < 0:
                key += self.iLength
            if key < 0 or key >= self.iLength:
                raise IndexError("Index out of range.")
            return self.szBuffer[key]
        else:
            raise TypeError("Invalid argument type; must be int or slice.")

    def __iter__(self):
        """
        Allow iteration over the characters of the built string.
        """
        for i in range(self.iLength):
            yield self.szBuffer[i]
