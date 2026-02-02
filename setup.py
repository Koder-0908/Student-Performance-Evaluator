from setuptools import find_packages, setup
from typing import List

E = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
    
        if E in requirements:
            requirements.remove(E)
    
    return requirements

setup(
    name = 'ML Project',
    version = '0.0.1',
    author = 'Kman',
    author_email = 'krish9pro@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt'))