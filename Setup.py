from setuptools import find_packages, setup
# find_packages functions is responsable to find all the packages availables in this ml project.
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    """
    This function will return the list of requirements
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements= [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
name='mlproject',
version='0.0.1',
author='J',
packages= find_packages(),
install_requires=get_requirements('requirements.txt'),


) nuevo_entorno
