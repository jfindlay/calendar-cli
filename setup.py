from setuptools import setup, find_packages

SRC_DIR = 'src'


def get_version():
    import sys

    sys.path[:0] = [SRC_DIR]
    return __import__('calendar_cli').__version__


setup(
    name='calendar-cli',
    version=get_version(),
    description='Fetch and notify daily summary for Google Calendar',
    author='mogproject',
    author_email='mogproj@gmail.com',
    license='Apache 2.0 License',
    url='https://github.com/mogproject/calendar-cli',
    install_requires=[
        'pyyaml',
        'six',
        'python-dateutil',
        'pytz',
        'google-api-python-client',
    ],
    tests_require=[
        'unittest2',
        'mock',
    ],
    package_dir={'': SRC_DIR},
    packages=find_packages(SRC_DIR),
    include_package_data=True,
    test_suite='tests',
    entry_points="""
    [console_scripts]
    calendar-cli = calendar_cli.calendar_cli:main
    """,
)