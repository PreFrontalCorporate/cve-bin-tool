# Copyright (C) 2025 Orange
# SPDX-License-Identifier: GPL-3.0-or-later

mapping_test_data = [
    {
        "product": "firejail",
        "version": "0.9.58.2",
        "version_strings": ["0.9.58.2\nfirejail version"],
    }
]
package_test_data = [
    {
        "url": "http://rpmfind.net/linux/fedora/linux/development/rawhide/Everything/aarch64/os/Packages/f/",
        "package_name": "firejail-0.9.72-7.fc42.aarch64.rpm",
        "product": "firejail",
        "version": "0.9.72",
    },
    {
        "url": "http://ftp.debian.org/debian/pool/main/f/firejail/",
        "package_name": "firejail_0.9.58.2-2+deb10u3_amd64.deb",
        "product": "firejail",
        "version": "0.9.58.2",
    },
    {
        "url": "https://dl-cdn.alpinelinux.org/alpine/v3.11/community/x86_64/",
        "package_name": "firejail-0.9.60-r0.apk",
        "product": "firejail",
        "version": "0.9.60",
        "other_products": ["gcc"],
    },
]
