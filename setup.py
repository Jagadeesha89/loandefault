"""
The setup.py file is an essential part of packaging and 
distirbuting python projects. It is used by setuptools
(or distutils in older python version) to define the configuration
of your projects, such as its meta data,dependencies,and more

"""

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines() ##read the line from file
            for line in lines: ##process each line
                requirement=line.strip() ##remove the empty space
                if requirement and requirement != "-e .":
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    
    return requirement_lst

setup(
    name="Loandefault",
    version="0.0.1",
    author="jagadeesha",
    author_email="jaga.m.gowda@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)

