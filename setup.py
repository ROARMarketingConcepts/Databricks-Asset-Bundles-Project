from setuptools import setup, find_packages

setup(
    name="dab_project",
    version="0.0.1",
    description="This contains the code in the ./src directory of the project",
    author="Ken Wood",
    packages=find_packages(where="./src"),
    package_dir={"":"./src"},
    install_requires=["setuptools"],
    entry_points={p
        "packages":[
            "main=dab_project.main:main"
        ]
    }
)
