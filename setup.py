from setuptools import setup

def get_install_requires() -> list[str]:
    """Returns requirements.txt parsed to a list"""
    fname = 'requirements.txt'
    targets = []
    if os.path.isfile(fname):
        with open(fname, 'r') as f:
            targets = f.read().splitlines()
    return targets

setup(
    name='distributions',
    version='1.0',
    description='Module to analyze distributions',
    author='stephlew24',
    packages=['distributions'],
    zipsafe=False,
    install_requires=get_install_requires()
)
