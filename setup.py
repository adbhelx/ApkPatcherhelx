import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ApkPatcher",
    version="2.0",
    author="RK_TECHNO_INDIA",
    author_email="TechnoIndia786@gmail.com",
    description="ApkPatcher Smali Patcher => Remove VPN Detect, Bypass SSL & Package Detection, Remove Debugging, Remove Ads, Spoof Device Info, AES Logs Injection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url="https://github.com/Technoindian/ApkPatcher",
    keywords='ApkPatcher',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
    entry_points={
        'console_scripts': [
            'ApkPatcher=ApkPatcher.__main__:RK_Techno_IND',
        ],
    },
)
