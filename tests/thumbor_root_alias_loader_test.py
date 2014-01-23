from unittest import TestCase
import thumbor_root_alias_loader


class ThumborRootAliasLoaderTestCase(TestCase):

    def test_validate(self):

        context = dotdictify({
            'config': {
                'ROOT_ALIAS_LOADER_URLS': {
                    '#3#': 'http://example.com'
                }
            }
        })

        url = "#3#/test.jpg"
        self.assertTrue(thumbor_root_alias_loader.validate(context, url))

        url = "#2#/test.jpg"
        self.assertFalse(thumbor_root_alias_loader.validate(context, url))

        url = "http://localhost/test.jpg"
        self.assertFalse(thumbor_root_alias_loader.validate(context, url))

    def test__prepare(self):

        context = dotdictify({
            'config': {
                'ROOT_ALIAS_LOADER_URLS': {
                    '#2#': 'http://test.com/added',
                    '#3#': 'http://example.com'
                }
            }
        })

        preparator = thumbor_root_alias_loader._prepare

        prepared = preparator(context, "#2#/path/to/test.jpg")
        self.assertEqual(prepared, "http://test.com/added/path/to/test.jpg")

        prepared = preparator(context, "#3#/test.jpg")
        self.assertEqual(prepared, "http://example.com/test.jpg")

        prepared = preparator(context, "haha not working")
        self.assertFalse(prepared)



class dotdictify(dict):
    """Transform a dictionary into an object
    http://stackoverflow.com/a/3031270/1014879
    """

    marker = object()

    def __init__(self, value=None):
        if value is None:
            pass
        elif isinstance(value, dict):
            for key in value:
                self.__setitem__(key, value[key])
        else:
            raise TypeError('expected dict')

    def __setitem__(self, key, value):
        if isinstance(value, dict) and not isinstance(value, dotdictify):
            value = dotdictify(value)
        dict.__setitem__(self, key, value)

    def __getitem__(self, key):
        found = self.get(key, dotdictify.marker)
        if found is dotdictify.marker:
            found = dotdictify()
            dict.__setitem__(self, key, found)
        return found

    __setattr__ = __setitem__
    __getattr__ = __getitem__


