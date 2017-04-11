import pytest
import os

from python_voc_parser import utils

class TestUtils:
    """ Test for utils.py."""
    def test_no_file(self):
        """ Test the function raises an exception with no real file"""
        with pytest.raises(FileNotFoundError):
            utils.get_file_lines('no_real_file')

    def test_lines(self, tmpdir):
        """ This test creates a tmp file with some dummy lines and test it is read correctly
            see: https://docs.pytest.org/en/latest/tmpdir.html
         """

        # create a dummy file with one line
        p = tmpdir.mkdir("sub").join("test.txt")
        p.write("content1")

        # parse the file
        result = utils.get_file_lines(str(p.realpath()))

        assert type(result) == list, "It should return a list"
        assert result == ["content1"], "It should read each line from a file a return a list with the lines"

    def test_not_written(self):
        """ dummy """
        pytest.skip("This should test something that is not writtent yet.")
