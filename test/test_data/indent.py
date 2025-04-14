# Copyright (C) 2025 Orange
# SPDX-License-Identifier: GPL-3.0-or-later

mapping_test_data = [
    {"product": "indent", "version": "2.2.12", "version_strings": ["GNU indent 2.2.12"]}
]
package_test_data = [
    {
        "url": "http://rpmfind.net/linux/fedora/linux/development/rawhide/Everything/aarch64/os/Packages/i/",
        "package_name": "indent-2.2.13-9.fc42.aarch64.rpm",
        "product": "indent",
        "version": "2.2.13",
    },
    {
        "url": "http://ftp.debian.org/debian/pool/main/i/indent/",
        "package_name": "indent_2.2.12-1_amd64.deb",
        "product": "indent",
        "version": "2.2.12",
    },
    {
        "url": "https://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/",
        "package_name": "indent-2.2.12-r0.apk",
        "product": "indent",
        "version": "2.2.12",
        "other_products": ["gcc"],
    },
]
