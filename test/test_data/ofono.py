# Copyright (C) 2025 Orange
# SPDX-License-Identifier: GPL-3.0-or-later

mapping_test_data = [
    {"product": "ofono", "version": "1.21", "version_strings": ["OFONO_LABEL\n1.21"]}
]
package_test_data = [
    {
        "url": "http://rpmfind.net/linux/fedora/linux/development/rawhide/Everything/aarch64/os/Packages/o/",
        "package_name": "ofono-2.16-1.fc43.aarch64.rpm",
        "product": "ofono",
        "version": "2.16",
    },
    {
        "url": "http://ftp.debian.org/debian/pool/main/o/ofono/",
        "package_name": "ofono_1.21-1_amd64.deb",
        "product": "ofono",
        "version": "1.21",
    },
    {
        "url": "https://dl-cdn.alpinelinux.org/alpine/v3.16/community/x86_64/",
        "package_name": "ofono-1.34-r0.apk",
        "product": "ofono",
        "version": "1.34",
        "other_products": ["gcc"],
    },
]
