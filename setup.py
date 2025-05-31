#!/usr/bin/env python3
"""
Setup script for JEE Progress Tracker
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="jee-progress-tracker",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A comprehensive progress tracking tool for JEE preparation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/jee-progress-tracker",
    py_modules=["jee_tracker"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Topic :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "jee-tracker=jee_tracker:main",
        ],
    },
    keywords="jee, education, progress-tracking, exam-preparation, study-planner",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/jee-progress-tracker/issues",
        "Source": "https://github.com/yourusername/jee-progress-tracker",
        "Documentation": "https://github.com/yourusername/jee-progress-tracker#readme",
    },
)
