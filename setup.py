from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pynse',  
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/boyalasaiganesh', 
    include_package_data=True,
    author='sai ganesh',
    author_email='saiganesh3131@gmail.com',
    description='A Streamlit app for analyzing NSE data',
    long_description_content_type="text/markdown",
    long_description=long_description,
    install_requires=[
        'streamlit',
        'requests',
        'fake-headers',
        'beautifulsoup4',
        'pandas',
        'matplotlib',
        'mplfinance',
        'plotly',
        'pynse'  # Assuming this is your library
    ],
    keywords=['NSE', 'Stock Market', 'Finance', 'Data Analysis'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Adjust based on your requirements
)
