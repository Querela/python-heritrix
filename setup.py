from distutils.core import setup

setup(
    name="python-heritrix",
    py_modules=["heritrix"],
    version="0.2",
    description="Simple wrapper around Heritrix v3 API",
    install_requires=["requests", "lxml"],
    license=open("LICENSE.txt").read(),
    author="Daniel Chudnov",
    author_email="dchud@gwu.edu",
    url="https://github.com/gwu-libraries/python-heritrix",
    keywords=["heritrix"],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
    ],
)
