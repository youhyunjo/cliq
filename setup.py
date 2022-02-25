import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    author="youhyunjo",
    author_email="you@cpan.org",
    url="https://github.com/youhyunjo/cliq", 
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    entry_points = {
        'console_scripts': [
            'cliq=cliq.main.cli:main',
        ],
    },
)
