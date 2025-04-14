# Copyright (C) 2025 Keysight Technologies
# SPDX-License-Identifier: GPL-3.0-or-later

mapping_test_data = [
    {
        "product": "cairo",
        "version": "1.16.0",
        "version_strings": ["../../cairo-1.16.0/src/cairo-analysis-surface.c"],
    }
]
package_test_data = [
    {
        "url": "https://mirror.msys2.org/mingw/ucrt64/",
        "package_name": "mingw-w64-ucrt-x86_64-cairo-1.18.2-2-any.pkg.tar.zst",
        "product": "cairo",
        "version": "1.18.2",
        "other_products": ["gcc"],
    },
    {
        "url": "http://rpmfind.net/linux/fedora/linux/development/rawhide/Everything/aarch64/os/Packages/c/",
        "package_name": "cairo-1.18.2-3.fc42.aarch64.rpm",
        "product": "cairo",
        "version": "1.18.2",
    },
    {
        "url": "http://ftp.fr.debian.org/debian/pool/main/c/cairo/",
        "package_name": "libcairo2_1.16.0-4+deb10u1_amd64.deb",
        "product": "cairo",
        "version": "1.16.0",
    },
    {
        "url": "https://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/",
        "package_name": "cairo-1.16.0-r3.apk",
        "product": "cairo",
        "version": "1.16.0",
        "other_products": ["gcc"],
    },
]
