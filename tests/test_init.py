"""
Basic tests for coursera package initialization.
"""

import unittest
from coursera import __version__, __author__


class TestCourseraInit(unittest.TestCase):
    """Test coursera package initialization."""

    def test_version_exists(self):
        """Test that version is defined."""
        self.assertIsNotNone(__version__)
        self.assertEqual(__version__, '0.1.0')

    def test_author_exists(self):
        """Test that author is defined."""
        self.assertIsNotNone(__author__)
        self.assertEqual(__author__, 'Coursera')


if __name__ == '__main__':
    unittest.main()
