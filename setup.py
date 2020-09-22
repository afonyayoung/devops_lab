from setuptools import setup, find_packages

setup(
    name="snapshot",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "snapshot = snapshot.snapshot",
        ],
    },
    install_requires=[
        'psutil',
        'argparse',
        'schedule',
        'datetime'
    ],
    version="0.1",
    author="Alexey Afanasenko",
    author_email="some@gmail.com",
    description="Example of the test application",
    license="MIT",
)
