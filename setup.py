from setuptools import setup, find_packages

setup(
    name="tradewise",
    version="0.1.0",
    description="Trading Strategies",
    author="Anurag Modi",
    author_email="modi.anurag1992@gmail.com",
    url="https://github.com/anurag3753/tradewise",
    packages=find_packages(),
    install_requires=[
        'yfinance',
        'pandas',
        # Add any other dependencies your project requires
    ],
)
