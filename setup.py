from setuptools import setup, find_packages

setup(
    name="health-agent-lab",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "strands-agents>=0.1.7",
        "strands-agents-builder>=0.1.3",
        "strands-agents-tools>=0.1.5",
    ],
) 