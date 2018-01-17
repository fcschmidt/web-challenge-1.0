from setuptools import setup, find_packages

requires = [
    'pyramid',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    ]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',  # includes virtualenv
    'pytest-cov',
    ]

setup(name='quotes_app',
      version='0.0',
      description='Web Challenge 1.0 - Consumer and Create RestFull API with Pyramid',
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
          "Topic :: Internet :: WWW/HTTP :: RESTful API"
      ],
      license='MIT - https://opensource.org/licenses/MIT',
      author='https://twitter.com/fcschimidt',
      author_email='mail@fcschmidt.me',
      url='https://github.com/fcschmidt/web-challenge-1.0',
      keywords='web wsgi bfg pylons pyramid restful api',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      extras_require={
          'testing': tests_require,
      },
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = quotes_app:main
      [console_scripts]
      initialize_quotes_app_db = quotes_app.scripts.initialize_db:main
      """,
      )
