import os
import sys
import time
import pytest

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.elements_page import TextBoxPage


@pytest.mark.usefixtures("driver")
class TestElements:

    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, url="https://demoqa.com/text-box")
            text_box_page.open()
            input_data = text_box_page.fill_all_fields()
            time.sleep(2)
            output_data = text_box_page.check_filled_form_fields()
            time.sleep(2)
            assert input_data == output_data
