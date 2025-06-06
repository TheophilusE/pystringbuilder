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

    def test_trim_start_no_whitespace(self):
        sb = StringBuilder()
        sb.append("Hello, world!")
        sb.trim_start()
        self.assertEqual(str(sb), "Hello, world!")

    def test_trim_start_leading_whitespace(self):
        sb = StringBuilder()
        sb.append("   Hello")
        sb.trim_start()
        self.assertEqual(str(sb), "Hello")

    def test_trim_start_mixed_whitespace(self):
        sb = StringBuilder()
        sb.append("\t  Hello")
        sb.trim_start()
        self.assertEqual(str(sb), "Hello")

    def test_trim_start_large_string(self):
        sb = StringBuilder()
        sb.append(" " * 2000 + "Hello")
        sb.trim_start()
        self.assertEqual(str(sb), "Hello")

    def test_trim_start_empty_buffer(self):
        sb = StringBuilder()
        sb.trim_start()
        self.assertEqual(str(sb), "")

    def test_trim_start_all_whitespace(self):
        sb = StringBuilder()
        sb.append("     ")
        sb.trim_start()
        self.assertEqual(str(sb), "")

    def test_trim_end_no_whitespace(self):
        sb = StringBuilder()
        sb.append("Hello, world!")
        sb.trim_end()
        self.assertEqual(str(sb), "Hello, world!")

    def test_trim_end_trailing_whitespace(self):
        sb = StringBuilder()
        sb.append("Hello   ")
        sb.trim_end()
        self.assertEqual(str(sb), "Hello")

    def test_trim_end_mixed_whitespace(self):
        sb = StringBuilder()
        sb.append("Hello \t  \n")
        sb.trim_end()
        self.assertEqual(str(sb), "Hello")

    def test_trim_end_large_string(self):
        sb = StringBuilder()
        sb.append("Hello" + " " * 2000)
        sb.trim_end()
        self.assertEqual(str(sb), "Hello")

    def test_trim_end_empty_buffer(self):
        sb = StringBuilder()
        sb.trim_end()
        self.assertEqual(str(sb), "")

    def test_trim_end_all_whitespace(self):
        sb = StringBuilder()
        sb.append("     ")
        sb.trim_end()
        self.assertEqual(str(sb), "")

    def test_substring(self):
        sb = StringBuilder()
        sb.append("Hello World")
        self.assertEqual(sb.substring(6, 11), "World")

    def test_find_exact_match(self):
        sb = StringBuilder()
        sb.append("Hello, this is a test string for find method.")
        self.assertEqual(sb.find("test"), 17)

    def test_find_partial_match(self):
        sb = StringBuilder()
        sb.append("Hello, this is a test string for find method.")
        self.assertEqual(sb.find("is"), 9)  # First occurrence of "is".

    def test_find_no_match(self):
        sb = StringBuilder()
        sb.append("Hello, this is a test string for find method.")
        self.assertEqual(sb.find("notfound"), -1)

    def test_find_empty_substring(self):
        sb = StringBuilder()
        sb.append("Hello, this is a test string for find method.")
        self.assertEqual(sb.find(""), 0)

    def test_find_single_character(self):
        sb = StringBuilder()
        sb.append("Hello, this is a test string for find method.")
        self.assertEqual(sb.find("t"), 7)

    def test_find_start_index(self):
        sb = StringBuilder()
        sb.append("Hello, this is a test string for find method.")
        self.assertEqual(sb.find("is", 11), 12)  # Finds the second occurrence of "is"

    def test_find_end_index(self):
        sb = StringBuilder()
        sb.append("Hello, this is a test string for find method.")
        self.assertEqual(sb.find("string", 0, 20), -1)  # "string" is at index 22 but limit is 20.

    def test_find_large_string_switching(self):
        sb = StringBuilder()
        sb.append("Hello, this is a test string for find method.")
        szLargeText = "A" * 2000 + "pattern" + "B" * 2000
        sb.clear()
        sb.append(szLargeText)
        self.assertEqual(sb.find("pattern"), 2000)

    def test_find_large_string_no_match(self):
        sb = StringBuilder()
        sb.append("Hello, this is a test string for find method.")
        szLargeText = "X" * 5000
        sb.clear()
        sb.append(szLargeText)
        self.assertEqual(sb.find("Y"), -1)

    def test_find_special_characters(self):
        sb = StringBuilder()
        sb.append("Hello, this is a test string for find method.")
        sb.append("!@#$%^&*()_+")
        self.assertEqual(sb.find("&*"), 51)  # Index where "&*" appears.

    def test_find_unicode(self):
        sb = StringBuilder()
        sb.append("Hello, this is a test string for find method.")
        sb.append("こんにちは世界")
        self.assertEqual(sb.find("世界"), 50)  # Index where "世界" appears.

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
