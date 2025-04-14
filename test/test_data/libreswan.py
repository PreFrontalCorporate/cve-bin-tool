# Copyright (C) 2025 Orange
# SPDX-License-Identifier: GPL-3.0-or-later

mapping_test_data = [
    {"product": "libreswan", "version": "3.32", "version_strings": ["libreswan-3.32"]}
]
package_test_data = [
    {
        "url": "http://rpmfind.net/linux/fedora/linux/development/rawhide/Everything/aarch64/os/Packages/l/",
        "package_name": "libreswan-5.1-5.fc42.aarch64.rpm",
        "product": "libreswan",
        "version": "5.1",
    },
    {
        "url": "http://ftp.debian.org/debian/pool/main/libr/libreswan/",
        "package_name": "libreswan_3.27-6+deb10u1_amd64.deb",
        "product": "libreswan",
        "version": "3.27",
    },
    {
        "url": "https://downloads.openwrt.org/releases/packages-19.07/x86_64/packages/",
        "package_name": "libreswan_3.32-1_x86_64.ipk",
        "product": "libreswan",
        "version": "3.32",
    },
    {
        "url": "https://dl-cdn.alpinelinux.org/alpine/v3.11/community/x86_64/",
        "package_name": "libreswan-3.29-r1.apk",
        "product": "libreswan",
        "version": "3.29",
        "other_products": ["gcc"],
    },
]
