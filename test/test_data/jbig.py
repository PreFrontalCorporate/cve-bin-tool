# Copyright (C) 2025 Keysight Technologies
# SPDX-License-Identifier: GPL-3.0-or-later

mapping_test_data = [
    {
        "product": "jbig-kit",
        "version": "2.1",
        "version_strings": [
            "JBIG-KIT 2.1 -- (c) 1995-2014 Markus Kuhn -- Licence: GPL"
        ],
    },
]
package_test_data = [
    {
        "url": "http://ftp.debian.org/debian/pool/main/j/jbigkit/",
        "package_name": "libjbig0_2.1-6.1+b2_amd64.deb",
        "product": "jbig-kit",
        "version": "2.1",
    },
    {
        "url": "https://mirror.msys2.org/mingw/ucrt64/",
        "package_name": "mingw-w64-ucrt-x86_64-jbigkit-2.1-5-any.pkg.tar.zst",
        "product": "jbig-kit",
        "version": "2.1",
        "other_products": ["gcc"],
    },
]
