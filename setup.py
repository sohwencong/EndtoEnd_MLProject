from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'  # assign variable
def get_requirements(file_path:str)->List[str]:  # return a list
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:  # temporary object
        requirements=file_obj.readlines()  # read object
        requirements=[req.replace('\n', '') for req in requirements]  # replace \n with blank

        if HYPEN_E_DOT in requirements:  # removes '-e .'
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='EndtoEnd_MLProject',
    version='0.0.1',
    author='Soh Wen Cong',
    author_email='sohbryon@gmail.com',
    packages=find_packages(),  # look for packages with __init__.py
    install_requires=get_requirements('requirements.txt')
)