from pyrus import backoff
import unittest
import time

class TestBackoff(unittest.TestCase):

    def test_backoff_with_no_retries(self):

        # Create a backoff object with no retries
        backoff = backoff(lambda: 1)

        # Call the backoff object
        result = backoff()

        # Assert that the result is 1
        self.assertEqual(result, 1)

    def test_backoff_with_one_retry(self):

        # Create a backoff object with one retry
        backoff = backoff(lambda: 1, max_retries=1)

        # Call the backoff object
        result = backoff()

        # Assert that the result is 1
        self.assertEqual(result, 1)

    def test_backoff_with_multiple_retries(self):

        # Create a backoff object with multiple retries
        backoff = backoff(lambda: 1, max_retries=3)

        # Call the backoff object multiple times
        for i in range(4):
            result = backoff()

        # Assert that the result is 1
        self.assertEqual(result, 1)

    def test_backoff_with_exponential_backoff(self):

        # Create a backoff object with exponential backoff
        backoff = self.backoff(lambda: 1, max_retries=3, backoff=2)

        # Call the backoff object multiple times
        for i in range(4):
            start = time.time()
            result = backoff()
            end = time.time()

            # Assert that the result is 1
            self.assertEqual(result, 1)

            # Assert that the time between retries increases exponentially
            self.assertGreater(end - start, i * backoff)


unittest.main()
