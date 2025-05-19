import unittest
from total_appearance import appearance  # Импорт твоей функции
from .import test  # Импорт тестов с корректными ответами


class AppearanceTests(unittest.TestCase):
    def test_all_cases(self):
        for i, case in enumerate(test.tests):
            with self.subTest(i=i):
                result = appearance(case["intervals"])
                self.assertEqual(result, case["answer"], f"Test #{i + 1} failed: got {result}, expected {case['answer']}")


if __name__ == "__main__":
    unittest.main()
