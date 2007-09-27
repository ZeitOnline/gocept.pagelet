# Copyright (c) 2007 gocept gmbh & co. kg
# See also LICENSE.txt
# $Id$

import os.path

from setuptools import setup, find_packages


setup(
    name = 'gocept.pagelet',
    version = "0.1",
    author = "Christian Zagrodnick",
    author_email = "cz@gocept.com",
    description = "Extensions for zope.formlib",
    long_description = file(os.path.join(os.path.dirname(__file__),
                                         'src', 'gocept', 'pagelet',
                                         'README.txt')).read(),
    license = "ZPL 2.1",
    url='http://pypi.python.org/pypi/gocept.pagelet',

    packages = find_packages('src'),
    package_dir = {'': 'src'},

    include_package_data = True,
    zip_safe = False,

    namespace_packages = ['gocept'],
    install_requires = [
        'setuptools',
        'zope.interface',
        'zope.component',
        'zope.publisher',
        'zope.viewlet',
        'z3c.template',
        'z3c.pagelet',
    ],
    extras_require = dict(
        test=['zope.testing'])
    )
