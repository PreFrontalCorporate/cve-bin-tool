# Copyright (C) 2025 Orange
# SPDX-License-Identifier: GPL-3.0-or-later

mapping_test_data = [
    {"product": "libcap", "version": "2.66", "version_strings": ["libcap-2.66"]}
]
package_test_data = [
    {
        "url": "http://rpmfind.net/linux/fedora/linux/development/rawhide/Everything/aarch64/os/Packages/l/",
        "package_name": "libcap-2.73-2.fc42.aarch64.rpm",
        "product": "libcap",
        "version": "2.73",
    },
    {
        "url": "http://ftp.debian.org/debian/pool/main/libc/libcap2/",
        "package_name": "libcap2_2.66-4_amd64.deb",
        "product": "libcap",
        "version": "2.66",
    },
    {
        "url": "https://dl-cdn.alpinelinux.org/alpine/v3.18/main/x86_64/",
        "package_name": "libcap2-2.69-r0.apk",
        "product": "libcap",
        "version": "2.69",
        "other_products": ["gcc"],
    },
]
