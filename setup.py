import setuptools
import unittest


def test_suite():
    return unittest.TestLoader().discover('tests', pattern='test_*.py')


setuptools.setup(
    name='jsondate',
    version='0.1.3',
    url='https://github.com/ilya-kolpakov/jsondate',
    license='MIT',
    author='Rick Harris',
    author_email='rconradharris@gmail.com',
    maintainer = 'Ilya Kolpakov',
    maintainer_email = 'ilya.kolpakov@gmail.com',
    description='JSON with datetime support',
    long_description=__doc__,
    packages=setuptools.find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['six'],
    test_suite='setup.test_suite',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
