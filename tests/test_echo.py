import unittest
import subprocess
import echo


class TestKatas(unittest.TestCase):

    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_upper(self):
        self.assertEqual(echo.convert_to_upper('hello world'), 'HELLO WORLD')

    def test_lower(self):
        self.assertEqual(echo.convert_to_lower('heLLo world'), 'hello world')

    def test_title(self):
        self.assertEqual(echo.convert_to_title('hEllo worlD'), 'Hello World')


if __name__ == '__main__':
    unittest.main()
