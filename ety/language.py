from .data import langs


class Language(object):
    def __init__(self, iso):
        self.iso = iso
        self.name = None

        for lang in langs:
            if lang['iso6393'] == iso:
                self.name = lang['name']

        if not self.name:
            raise ValueError('Language with iso code \'%s\' unknown' % iso)

    def __repr__(self):
        return u'Language(iso={})'.format(self.iso)

    def __str__(self):
        return self.name
