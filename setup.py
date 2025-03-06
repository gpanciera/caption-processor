from setuptools import setup, find_packages

setup(
    name="caption-processor",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'caption-processor=src.main:main',
        ],
    },
    description="A utility for processing SMPTE Timecode-based Captions",
    author="Your Name",
    author_email="your.email@example.com",
    python_requires='>=3.6',
)