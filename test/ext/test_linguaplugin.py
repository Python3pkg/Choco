import os
from .. import TemplateTest, template_base, skip_if

try:
    import lingua
except:
    lingua = None

if lingua is not None:
    from choco.ext.linguaplugin import LinguaChocoExtractor
    from lingua.extractors import register_extractors


class MockOptions:
    keywords = []
    domain = None


def skip():
    return skip_if(
        lambda: not lingua, 'lingua not installed: skipping linguaplugin test')


class ExtractChocoTestCase(TemplateTest):
    @skip()
    def test_extract(self):
        register_extractors()
        plugin = LinguaChocoExtractor({'comment-tags': 'TRANSLATOR'})
        messages = list(
            plugin(os.path.join(template_base, 'gettext.choco'), MockOptions()))
        msgids = [(m.msgid, m.msgid_plural) for m in messages]
        self.assertEqual(
            msgids,
            [
                ('Page arg 1', None),
                ('Page arg 2', None),
                ('Begin', None),
                ('Hi there!', None),
                ('Hello', None),
                ('Welcome', None),
                ('Yo', None),
                ('The', None),
                ('bunny', 'bunnies'),
                ('Goodbye', None),
                ('Babel', None),
                ('hella', 'hellas'),
                ('The', None),
                ('bunny', 'bunnies'),
                ('Goodbye, really!', None),
                ('P.S. byebye', None),
                ('Top', None),
                ('foo', None),
                ('hoho', None),
                ('bar', None),
                ('Inside a p tag', None),
                ('Later in a p tag', None),
                ('No action at a distance.', None)])
