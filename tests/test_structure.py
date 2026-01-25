"""
Tests for the Agentic BOM Engineering book repository.
"""
import os
import unittest


class BookStructureTests(unittest.TestCase):
    """Test that the book structure is valid."""
    
    def setUp(self):
        self.repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.book_dir = os.path.join(self.repo_root, 'book')
        
    def test_book_directory_exists(self):
        """Test that the book directory exists."""
        self.assertTrue(os.path.exists(self.book_dir), 
                       "Book directory should exist")
        
    def test_all_chapters_exist(self):
        """Test that all expected book chapters exist."""
        expected_chapters = [
            '00-foreword.md',
            '01-introduction.md',
            '02-current-state-bom-engineering-in-medtech.md',
            '03-agentic-engineering-foundations-for-bom.md',
            '04-unified-namespace-for-engineering-and-bom-events.md',
            '05-agent-types-and-patterns-for-bom-lifecycle.md',
            '06-engineering-as-a-service-model-for-bom-and-change.md',
            '07-implementation-roadmap.md',
            '08-metrics-and-value-realization.md',
            '09-regulation-validation-and-traceability.md',
            '10-case-studies-and-scenarios.md',
            '11-operating-model-and-org-change.md',
            '12-future-directions-and-next-steps.md',
        ]
        
        for chapter in expected_chapters:
            chapter_path = os.path.join(self.book_dir, chapter)
            self.assertTrue(os.path.exists(chapter_path),
                          f"Chapter {chapter} should exist")
                          
    def test_chapters_not_empty(self):
        """Test that all chapter files have content."""
        book_files = [f for f in os.listdir(self.book_dir) 
                     if f.endswith('.md')]
        
        for book_file in book_files:
            file_path = os.path.join(self.book_dir, book_file)
            with open(file_path, 'r') as f:
                content = f.read()
                self.assertTrue(len(content) > 0,
                              f"{book_file} should not be empty")
                              
    def test_readme_exists(self):
        """Test that README.md exists."""
        readme_path = os.path.join(self.repo_root, 'README.md')
        self.assertTrue(os.path.exists(readme_path),
                       "README.md should exist")


if __name__ == '__main__':
    unittest.main()
