import os
from setuptools import setup

# Utility function to read the README file.  
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "cupydle",
    version = "1.0",
    author = "Ponzoni Cuadra, Nelson E.",
    author_email = "npcuadra@gmail.com",
    description = ("Restricted Boltzmann Machines and Deep Belief Networks."),
    license = "BSD",
    keywords = "machine learning restricted boltzmann machine deep belief networks",
    url = "",
    packages=['rbm'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 1 - Production/Stable",
        "Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: BSD License",
    ],
)
