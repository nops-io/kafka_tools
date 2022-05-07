import time
from datetime import datetime

import setuptools

now = datetime.now()

setuptools.setup(
    name="kafka_tools",
    version=f"{now.year}.{now.month}.{now.day}.{now.hour}_{now.minute}",
    author="Nikita Zagorskiy",
    author_email="nikita@nops.io",
    description="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=["kafka-python>2.0.0", "msgpack>1.0.0"],
)
