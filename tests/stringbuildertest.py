import unittest

from pystringbuilder.stringbuilder import StringBuilder

class TestStringBuilder(unittest.TestCase):
    def test_append(self):
        sb = StringBuilder()
        sb.append("Hello")
        self.assertEqual(str(sb), "Hello")

    def test_append_line(self):
        sb = StringBuilder()
        sb.append_line("Hello")
        self.assertEqual(str(sb), "Hello\n")

    def test_insert(self):
        sb = StringBuilder()
        sb.append("Hello World")
        sb.insert(6, "Beautiful ")
        self.assertEqual(str(sb), "Hello Beautiful World")

    def test_delete(self):
        sb = StringBuilder()
        sb.append("Hello Beautiful World")
        sb.delete(6, 16)
        self.assertEqual(str(sb), "Hello World")

    def test_replace_simple(self):
        sb = StringBuilder()
        sb.append("Hello, world! Hello!")
        sb.replace("Hello", "Hi")
        self.assertEqual(str(sb), "Hi, world! Hi!")

    def test_replace_partial(self):
        sb = StringBuilder()
        sb.append("Hello, world! Hello!")
        sb.replace("lo", "XX")
        self.assertEqual(str(sb), "HelXX, world! HelXX!")

    def test_replace_no_match(self):
        sb = StringBuilder()
        sb.append("Hello, world! Hello!")
        sb.replace("Goodbye", "Hi")
        self.assertEqual(str(sb), "Hello, world! Hello!")

    def test_replace_empty_old(self):
        sb = StringBuilder()
        sb.append("Hello, world! Hello!")
        sb.replace("", "Hi")
        self.assertEqual(str(sb), "Hello, world! Hello!")

    def test_replace_large_string(self):
        sb = StringBuilder()
        sb.append("Hello, world! Hello!" * 500)
        sb.replace("Hello", "Greetings")
        self.assertEqual(str(sb), "Greetings, world! Greetings!" * 500)

    def test_reverse(self):
        sb = StringBuilder()
        sb.append("Python")
        sb.reverse()
        self.assertEqual(str(sb), "nohtyP")

    def test_trim_no_whitespace(self):
        sb = StringBuilder()
        sb.append("Hello, world!")
        sb.trim()
        self.assertEqual(str(sb), "Hello, world!")

    def test_trim_leading_whitespace(self):
        sb = StringBuilder()
        sb.append("   Hello")
        sb.trim()
        self.assertEqual(str(sb), "Hello")

    def test_trim_trailing_whitespace(self):
        sb = StringBuilder()
        sb.append("Hello   ")
        sb.trim()
        self.assertEqual(str(sb), "Hello")

    def test_trim_leading_and_trailing_whitespace(self):
        sb = StringBuilder()
        sb.append("   Hello   ")
        sb.trim()
        self.assertEqual(str(sb), "Hello")

    def test_trim_all_whitespace(self):
        sb = StringBuilder()
        sb.append("     ")
        sb.trim()
        self.assertEqual(str(sb), "")

    def test_trim_mixed_whitespace(self):
        sb = StringBuilder()
        sb.append("\t  Hello \n ")
        sb.trim()
        self.assertEqual(str(sb), "Hello")

    def test_trim_large_string(self):
        sb = StringBuilder()
        sb.append(" " * 2000 + "Hello" + " " * 2000)
        sb.trim()
        self.assertEqual(str(sb), "Hello")

    def test_trim_empty_buffer(self):
        sb = StringBuilder()
        sb.trim()
        self.assertEqual(str(sb), "")

    def test_trim_start(self):
        sb = StringBuilder()
        sb.append("   Hello World   ")
        sb.trim_start()
        self.assertEqual(str(sb), "Hello World   ")

    def test_trim_end(self):
        sb = StringBuilder()
        sb.append("   Hello World   ")
        sb.trim_end()
        self.assertEqual(str(sb), "   Hello World")

    def test_substring(self):
        sb = StringBuilder()
        sb.append("Hello World")
        self.assertEqual(sb.substring(6, 11), "World")

    def test_find(self):
        sb = StringBuilder()
        sb.append("Hello World")
        self.assertEqual(sb.find("World"), 6)

    def test_clear(self):
        sb = StringBuilder()
        sb.append("Hello")
        sb.clear()
        self.assertEqual(str(sb), "")

    def test_iadd(self):
        sb  = StringBuilder()
        sb += "Hello"
        sb += " World"
        self.assertEqual(str(sb), "Hello World")

    def test_add(self):
        sb1 = StringBuilder()
        sb1.append("Hello")
        sb2 = sb1 + " World"
        self.assertEqual(str(sb2), "Hello World")

    def test_getitem(self):
        sb = StringBuilder()
        sb.append("Hello World")
        self.assertEqual(sb[6], "W")       # Single character
        self.assertEqual(sb[:5], "Hello")  # Slice

    def test_iter(self):
        sb = StringBuilder()
        sb.append("Hello")
        charList = [char for char in sb]
        self.assertEqual(charList, ["H", "e", "l", "l", "o"])

if __name__ == "__main__":
    unittest.main()
