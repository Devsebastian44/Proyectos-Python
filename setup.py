from setuptools import find_packages, setup

setup(
    name="sysadmin_utils",
    version="1.0.0",
    description="A professional suite of system administration and security tools.",
    author="Your Name",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "mysql-connector-python>=9.6.0",
        "pandas>=2.2.3",
        "psutil>=5.8.0",
        "winotify>=1.0.4; sys_platform == 'win32'",
        "pysmb>=1.2.7",
        "pyautogui>=0.9.53",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.10",
)
