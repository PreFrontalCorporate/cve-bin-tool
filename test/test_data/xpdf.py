# Copyright (C) 2025 Orange
# SPDX-License-Identifier: GPL-3.0-or-later

mapping_test_data = [
    {"product": "xpdf", "version": "3.04", "version_strings": ["Xpdf\n3.04"]}
]
package_test_data = [
    {
        "url": "http://rpmfind.net/linux/fedora/linux/development/rawhide/Everything/aarch64/os/Packages/x/",
        "package_name": "xpdf-4.05-6.fc42.aarch64.rpm",
        "product": "xpdf",
        "version": "4.05",
    },
    {
        "url": "http://ftp.debian.org/debian/pool/main/x/xpdf/",
        "package_name": "xpdf_3.04-13_amd64.deb",
        "product": "xpdf",
        "version": "3.04",
    },
    {
        "url": "https://dl-cdn.alpinelinux.org/alpine/v3.11/community/x86_64/",
        "package_name": "xpdf-3.04-r4.apk",
        "product": "xpdf",
        "version": "3.04",
        "other_products": ["gcc"],
    },
]
