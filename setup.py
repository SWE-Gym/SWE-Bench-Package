import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='swegym',
    author='Jiayi Pan, Xingyao Wang',
    description='Fork of SWE-bench package - a benchmark for evaluating LMs on software engineering',
    keywords='nlp, benchmark, code',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/SWE-Gym/SWE-Gym',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    install_requires=[
        'beautifulsoup4',
        'chardet',
        'datasets',
        'docker',
        'ghapi',
        'GitPython',
        'pre-commit',
        'python-dotenv',
        'requests',
        'rich',
        'unidiff',
        'tqdm',
    ],
    extras_require={
        'inference': [
            'tiktoken',
            'openai',
            'anthropic',
            'transformers',
            'peft',
            'sentencepiece',
            'protobuf',
            'torch',
            'flash_attn',
            'triton',
            'jedi',
            'tenacity',
        ],
    },
    include_package_data=True,
)
