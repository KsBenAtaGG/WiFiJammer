#!/usr/bin/env python2
from setuptools import setup

setup(
    name = "wifijammer",
    version = "0.1",
    author = "Atakan Doğan Özban",
    description = "Continuously jam all wifi clients and access points within range.",
    keywords = "WiFi 802.11 jammer deauth",
    url = "https://github.com/KsBenAtaGG/WifiJammer",
    scripts=['wifijammer'],
    # py_modules=['wifijammer'],
    install_requires=['scapy'],
    long_description="Continuously jam all wifi clients and access points within range.",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
)
