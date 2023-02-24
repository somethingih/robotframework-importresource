from setuptools import setup

LIBRARY_NAME = "ImportResource"

setup(
    name="robotframework-%s" % LIBRARY_NAME.lower(),
    description="Tool to import robotframework resource files from python packages",
    url="https://github.com/rasjani/robotframework-%s" % LIBRARY_NAME.lower(),
    author="Jani Mikkonen",
    author_email="jani.mikkonen@gmail.com",
    license="Apache License 2.0",
    install_requires=[
        "robotframework",
    ],
    keywords="robot framework testing automation",
    platforms="any",
    packages=[LIBRARY_NAME],
    include_package_data=True,
)
