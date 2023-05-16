from . import *

class TestNormalise(unittest.TestCase):

    def test_normalise(self):

        test_cases = [(), (), ()]

        for i, (data, expected_output) in enumerate(test_cases):
            with self.subTest(test_case=i):
                n = Normalise(data)
                result = n.normalise()
                self.assertEqual(result, expected_output)


    def test_normalise_string(self):
        
        test_cases = [
            ("   HELLO! HOW ARE YOU?    ", "hello! how are you?"),
            ("Thé quick brøwn fóx jumps ovér the lazy dóg.", "the quick brown fox jumps over the lazy dog."),
            ("  Hello    world   ", "hello world"),
        ]
        
        for i, (data, expected_output) in enumerate(test_cases):
            with self.subTest(test_case=i):
                n = NormaliseString(data)
                result = n.normalise()
                self.assertEqual(result, expected_output)

unittest.main()