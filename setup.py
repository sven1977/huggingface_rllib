from setuptools import setup

install_requires = [
    "huggingface_hub",
    "cloudpickle==1.6",
    "pickle5",
    "pyyaml==6.0",
    "wasabi"
]

extras = {}

extras["quality"] = [
    "black~=22.0",
    "isort>=5.5.4",
    "flake8>=3.8.3",
]

setup(
    name='huggingface_rllib',
    version='0.0.1',
    packages=['huggingface_rllib'],
    url='https://github.com/sven1977/huggingface_rllib',
    license='Apache',
    author='Sven Mika, Thomas Simonini, and Hugging Face Team',
    author_email='sven@anyscale.com',
    description='Additional code for RLlib to load and upload models from the Hub.',
    install_requires=install_requires,
    extras_require=extras,
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords="reinforcement learning deep reinforcement learning RL",
)

