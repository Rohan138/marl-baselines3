from setuptools import setup

VERSION = "0.0.1"

long_description = ""
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

license = ""
with open("LICENSE.md", "r", encoding="utf-8") as fh:
    license = fh.read()

requirements = []
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.readlines()

setup(
    name="marl-baselines3",
    version=VERSION,
    description="Multi-Agent Reinforcement Learning with Stable-Baselines3",
    url="https://github.com/Rohan138/marl-baselines3",
    author="Rohan Potdar",
    author_email="rohanpotdar138@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license=license,
    packages=["marl_baselines3"],
    install_requires=requirements,
    python_requires=">=3.7, <3.10",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
