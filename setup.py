# coding: utf-8

from setuptools import setup


setup(name='easygpg',
      description='Easy-to-use GnuPG command-line interface',
      long_description=open('README.md').read(),
      version='0.1.0-dev',
      author=u'Álvaro Justen',
      author_email='alvarojusten@gmail.com',
      url='https://github.com/turicas/easygpg/',
      py_modules=['easygpg'],
      install_requires=['click'],
      keywords=['gpg', 'gnupg', 'cli', 'key', 'security'],
      entry_points = {
          'console_scripts': [
              'easygpg = easygpg:cli',
              'egpg = easygpg:cli',
              ],
      },
      classifiers = [
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
      ]
)
