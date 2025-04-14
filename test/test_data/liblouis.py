# Copyright (C) 2025 Orange
# SPDX-License-Identifier: GPL-3.0-or-later

mapping_test_data = [
    {"product": "liblouis", "version": "3.8.0", "version_strings": ["liblouis\n3.8.0"]}
]
package_test_data = [
    {
        "url": "http://rpmfind.net/linux/fedora/linux/development/rawhide/Everything/aarch64/os/Packages/l/",
        "package_name": "liblouis-3.28.0-8.fc42.aarch64.rpm",
        "product": "liblouis",
        "version": "3.28.0",
    },
    {
        "url": "http://ftp.debian.org/debian/pool/main/libl/liblouis/",
        "package_name": "liblouis17_3.8.0-2_amd64.deb",
        "product": "liblouis",
        "version": "3.8.0",
    },
    {
        "url": "https://dl-cdn.alpinelinux.org/alpine/v3.20/community/x86/",
        "package_name": "liblouis-3.29.0-r0.apk",
        "product": "liblouis",
        "version": "3.29.0",
        "other_products": ["gcc"],
    },
]
