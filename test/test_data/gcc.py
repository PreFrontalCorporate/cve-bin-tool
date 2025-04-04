# Copyright (C) 2021 Intel Corporation
# SPDX-License-Identifier: GPL-3.0-or-later

mapping_test_data = [
    {
        "product": "gcc",
        "version": "9.3.1",
        "version_strings": ["GCC: (GNU) 9.3.1"],
    },
    {
        "product": "gcc",
        "version": "9.1",
        "version_strings": ["GCC: (GNU) 9.1"],
    },
    {
        "product": "gcc",
        "version": "8.2.0",
        "version_strings": ["GCC: (Rev3, Built by MSYS2 project) 8.2.0"],
    },
]
package_test_data = [
    {
        "url": "http://mirrors.kernel.org/fedora/releases/33/Everything/x86_64/os/Packages/g/",
        "package_name": "gcc-10.2.1-3.fc33.x86_64.rpm",
        "product": "gcc",
        "version": "10.2.1",
    },
    {
        "url": "http://mirror.centos.org/centos/8/AppStream/x86_64/os/Packages/",
        "package_name": "gcc-8.4.1-1.el8.x86_64.rpm",
        "product": "gcc",
        "version": "8.4.1",
    },
    {
        "url": "https://mirror.msys2.org/mingw/ucrt64/",
        "package_name": "mingw-w64-ucrt-x86_64-zlib-1.3.1-1-any.pkg.tar.zst",
        "product": "gcc",
        "version": "13.2.0",
        "other_products": ["zlib"],
    },
]
