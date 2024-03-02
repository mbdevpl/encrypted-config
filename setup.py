"""Setup script for encrypted_config package."""

import boilerplates.setup


class Package(boilerplates.setup.Package):
    """Package metadata."""

    name = 'encrypted-config'
    description = 'Read and write partially encrypted configuration files.'
    url = 'https://github.com/mbdevpl/encrypted-config'
    classifiers = [
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Communications :: File Sharing',
        'Topic :: Security :: Cryptography',
        'Topic :: Utilities']
    keywords = ['config', 'encryption', 'rsa', 'security']


if __name__ == '__main__':
    Package.setup()
