import unittest
from src.components.validators.validate_url import UrlValidator

class TestUrlValidator(unittest.TestCase):
    def test_valid_url(self):
        urlValidator = UrlValidator()
        valid1 = "https://www.youtube.com/watch?v=j82L3pLjb_0"
        self.assertTrue(urlValidator.is_valid_url(valid1))

        valid2 = "https://www.youtube.com/embed/DFYRQ_zQ-gk"
        self.assertTrue(urlValidator.is_valid_url(valid2))

    def test_invalid_url(self):
        urlValidator = UrlValidator()
        invalid1 = "https://google.be/dQw4w9WgXcR"
        self.assertFalse(urlValidator.is_valid_url(invalid1))

        invalid2 = "https://rapidapi.com/blog/how-to-get-youtube-api-key/"
        self.assertFalse(urlValidator.is_valid_url(invalid2))


if __name__ == '__main__':
    unittest.main()

