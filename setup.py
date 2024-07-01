from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="aicoretools",
    version="0.0.2",
    author="CommMate",
    author_email="contact@commmate.com",
    description="A library for integrating AI API tools.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/commmate/aicoretools",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Creative Commons Attribution-NonCommercial 4.0 International License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
    install_requires=[
        'openai',
        'youtube_transcript_api',
        'beautifulsoup4',  # Use the full name for bs4
        'fpdf',
        'arrow',
        'googlemaps',
        'pytest',
    ],
)
