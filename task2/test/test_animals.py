import unittest
from unittest.mock import patch, Mock

# ВАЖНО: импорт с учётом структуры
from task2.solution.main import parse_animals_by_letter


class TestAnimalParser(unittest.TestCase):

    def test_output_structure(self):
        """Проверяет, что возвращается словарь с ключами-буквами и целочисленными значениями."""
        with patch("task2.solution.main.requests.get") as mock_get:
            mock_html = """
            <div id="mw-content-text" class="mw-body-content">
              <div class="mw-category mw-category-columns">
                <div class="mw-category-group">
                  <ul>
                    <li>Аист</li>
                    <li>Антилопа</li>
                  </ul>
                </div>
              </div>
              <div id="mw-pages">
              </div>
            </div>
            """
            mock_response = Mock()
            mock_response.text = mock_html
            mock_get.return_value = mock_response

            result = parse_animals_by_letter(alphabet=["А"])
            self.assertIsInstance(result, dict)
            self.assertIn("А", result)
            self.assertEqual(result["А"], 2)

    def test_break_on_different_letter(self):
        """Проверяет, что цикл прерывается, если имя животного не на нужную букву."""
        with patch("task2.solution.main.requests.get") as mock_get:
            mock_html = """
            <div id="mw-content-text" class="mw-body-content">
              <div class="mw-category mw-category-columns">
                <div class="mw-category-group">
                  <ul>
                    <li>Бобр</li>
                  </ul>
                </div>
              </div>
              <div id="mw-pages">
              </div>
            </div>
            """
            mock_response = Mock()
            mock_response.text = mock_html
            mock_get.return_value = mock_response

            result = parse_animals_by_letter(alphabet=["А"])
            self.assertEqual(result["А"], 0)

    def test_pagination_handling(self):
        """Проверяет обработку 'Следующая страница' и подсчёт с двух страниц."""
        with patch("task2.solution.main.requests.get") as mock_get:
            first_page = """
            <div id="mw-content-text" class="mw-body-content">
              <div class="mw-category mw-category-columns">
                <div class="mw-category-group">
                  <ul>
                    <li>Акула</li>
                  </ul>
                </div>
              </div>
              <div id="mw-pages">
                <a href="/wiki/page2">Следующая страница</a>
              </div>
            </div>
            """
            second_page = """
            <div id="mw-content-text" class="mw-body-content">
              <div class="mw-category mw-category-columns">
                <div class="mw-category-group">
                  <ul>
                    <li>Анаконда</li>
                    <li>Аист</li>
                  </ul>
                </div>
              </div>
              <div id="mw-pages">
              </div>
            </div>
            """
            mock_response_1 = Mock()
            mock_response_1.text = first_page

            mock_response_2 = Mock()
            mock_response_2.text = second_page

            mock_get.side_effect = [mock_response_1, mock_response_2]

            result = parse_animals_by_letter(alphabet=["А"])
            self.assertEqual(result["А"], 3)


if __name__ == "__main__":
    unittest.main()
