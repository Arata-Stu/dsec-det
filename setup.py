from distutils.core import setup

def parse_requirements(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()

setup(
    name='dsec_det',
    packages=['dsec_det'],
    package_dir={'': 'src'},
    install_requires=parse_requirements('requirements.txt')
)
