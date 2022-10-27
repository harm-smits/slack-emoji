import pathlib
import sys
import os
import unittest
import re


class EmojiFileTests(unittest.TestCase):
    files = []

    def setUp(self):
        target = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'emojis')
        print(target)
        self.files = pathlib.Path(target).glob('**/*')

    def test_files(self):
        names = {}

        regex = re.compile('^[a-z0-9-_]*$')

        for file in self.files:
            if not file.is_file():
                continue

            self.assertTrue(
                file.suffix in {".gif", ".png", ".jpg", ".jpeg"},
                "Emoji %s needs to be a gif, png or jpg." % file.resolve()
            )

            self.assertTrue(
                file.stat().st_size < 128 * 1024,
                "Emoji %s exceeds the limit of 128kb. Size is %d bytes." % (file.resolve(), file.stat().st_size)
            )

            self.assertTrue(
                file.stem not in names,
                "Emoji '%s' previously defined at '%s'." % (file.stem, names[file.stem] if file.stem in names else '')
            )

            names[file.stem] = file.resolve()

            self.assertTrue(
                regex.match(file.stem),
                "Emoji %s may only consist out of ascii characters, numbers, dash and underscore." % file.stem
            )


def test_suite():
    return unittest.findTestCases(sys.modules[__name__])


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
