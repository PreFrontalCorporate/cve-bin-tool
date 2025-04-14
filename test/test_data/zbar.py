# Copyright (C) 2025 Orange
# SPDX-License-Identifier: GPL-3.0-or-later

mapping_test_data = [
    {"product": "zbar", "version": "0.23", "version_strings": ["0.23\nzbar"]}
]
package_test_data = [
    {
        "url": "http://rpmfind.net/linux/fedora/linux/development/rawhide/Everything/aarch64/os/Packages/z/",
        "package_name": "zbar-0.23.93-6.fc42.aarch64.rpm",
        "product": "zbar",
        "version": "0.23.93",
    },
    {
        "url": "http://ftp.debian.org/debian/pool/main/z/zbar/",
        "package_name": "zbar-tools_0.23.90-1+deb11u1_amd64.deb",
        "product": "zbar",
        "version": "0.23.90",
    },
    {
        "url": "https://dl-cdn.alpinelinux.org/alpine/v3.11/community/x86_64/",
        "package_name": "zbar-0.23-r2.apk",
        "product": "zbar",
        "version": "0.23",
        "other_products": ["gcc"],
    },
]
