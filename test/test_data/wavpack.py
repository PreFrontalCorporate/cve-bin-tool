# Copyright (C) 2025 Orange
# SPDX-License-Identifier: GPL-3.0-or-later

mapping_test_data = [
    {"product": "wavpack", "version": "5.1.0", "version_strings": ["5.1.0\nlibwavpack"]}
]
package_test_data = [
    {
        "url": "http://rpmfind.net/linux/fedora/linux/development/rawhide/Everything/aarch64/os/Packages/w/",
        "package_name": "wavpack-5.7.0-11.fc42.aarch64.rpm",
        "product": "wavpack",
        "version": "5.7.0",
    },
    {
        "url": "http://ftp.debian.org/debian/pool/main/w/wavpack/",
        "package_name": "wavpack_5.4.0-1_arm64.deb",
        "product": "wavpack",
        "version": "5.4.0",
    },
    {
        "url": "https://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/",
        "package_name": "wavpack-5.1.0-r8.apk",
        "product": "wavpack",
        "version": "5.1.0",
        "other_products": ["gcc"],
    },
]
