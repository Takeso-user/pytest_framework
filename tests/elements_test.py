import os
import sys
import time
import pytest

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.elements_page import TextBoxPage, CheckboxPage

BASE_URL = (os.getenv('BASE_URL'))


@pytest.mark.usefixtures("driver")
class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            url = BASE_URL + 'text-box/'
            text_box_page = TextBoxPage(driver, url=url)
            text_box_page.open()
            input_name, input_email, input_current_address, input_permanent_address = (
                text_box_page.fill_all_fields())
            output_name, output_email, output_current_address, output_permanent_address = (
                text_box_page.check_filled_form_fields())
            time.sleep(2)
            assert input_name == output_name, "The full name is not match"
            assert input_email == output_email, "The email is not match"
            assert input_current_address == output_current_address, "The current address is not match"
            assert input_permanent_address == output_permanent_address, "The permanent address is not match"

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckboxPage(driver, url=os.getenv('BASE_URL') + 'checkbox/')
            check_box_page.open()
            check_box_page.check_checkbox()
            expected_list = ['home',
                             'desktop',
                             'notes',
                             'commands',
                             'documents',
                             'workspace',
                             'react',
                             'angular',
                             'veu',
                             'office',
                             'public',
                             'private',
                             'classified',
                             'general',
                             'downloads',
                             'wordFile',
                             'excelFile']
            for expected_item in expected_list:
                assert expected_item in check_box_page.check_result_items()

            time.sleep(2)
