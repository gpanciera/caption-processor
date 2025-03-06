import unittest
from src.processor import process_captions

class TestCaptionProcessor(unittest.TestCase):

    def test_single_speaker(self):
        input_text = "00:00:01:00\nSpeaker 1\nHello, this is a test.\n\n"
        expected_output = "**Speaker 1**: Hello, this is a test."
        self.assertEqual(process_captions(input_text), expected_output)

    def test_multiple_speakers(self):
        input_text = (
            "00:00:01:00\nSpeaker 1\nHello, this is a test.\n\n"
            "00:00:02:00\nSpeaker 2\nThis is another test.\n\n"
        )
        expected_output = "**Speaker 1**: Hello, this is a test. **Speaker 2**: This is another test."
        self.assertEqual(process_captions(input_text), expected_output)

    def test_same_speaker(self):
        input_text = (
            "00:00:01:00\nSpeaker 1\nHello, this is a test.\n\n"
            "00:00:02:00\nSpeaker 1\nAnd this is a continuation.\n\n"
        )
        expected_output = "**Speaker 1**: Hello, this is a test. And this is a continuation."
        self.assertEqual(process_captions(input_text), expected_output)

    def test_blank_lines(self):
        input_text = (
            "00:00:01:00\nSpeaker 1\nHello, this is a test.\n\n"
            "\n"
            "00:00:02:00\nSpeaker 2\nThis is another test.\n\n"
        )
        expected_output = "**Speaker 1**: Hello, this is a test. **Speaker 2**: This is another test."
        self.assertEqual(process_captions(input_text), expected_output)

    def test_no_input(self):
        input_text = ""
        expected_output = ""
        self.assertEqual(process_captions(input_text), expected_output)

if __name__ == '__main__':
    unittest.main()