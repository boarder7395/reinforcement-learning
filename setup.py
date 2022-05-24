from setuptools import setup, find_packages

requirements = [
    'keras==2.2.4',
    'tensorflow-gpu==2.6.4',
    'argparse==1.2.1',
    'gym==0.13.1',
]

setup(
    name='reinforcement_learning',
    version='0.0.0',
    packages=find_packages(include=['reinforcement_learning',
                                    'reinforcement_learning.*']),
    install_requires=requirements,
    )
