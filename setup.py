from setuptools import find_packages, setup

setup(
    name="beit3-gml",
    version="0.1.3",
    author="Gimlet Labs",
    url="https://github.com/gimletlabs/unilm",
    license="MIT",
    description="Package for beit3, part of UniLM by Microsoft, customized for GML tasks",
    packages=find_packages(where=".", include=["beit3"]),
    install_requires=open("beit3/requirements.txt").read().splitlines(),
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
