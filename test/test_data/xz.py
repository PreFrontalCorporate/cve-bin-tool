# Copyright (C) 2025 Orange
# SPDX-License-Identifier: GPL-3.0-or-later

mapping_test_data = [
    {"product": "xz", "version": "5.2.5", "version_strings": ["xz (XZ Utils) 5.2.5"]}
]
package_test_data = [
    {
        "url": "http://rpmfind.net/linux/fedora/linux/development/rawhide/Everything/aarch64/os/Packages/x/",
        "package_name": "xz-5.6.3-3.fc42.aarch64.rpm",
        "product": "xz",
        "version": "5.6.3",
    },
    {
        "url": "http://ftp.debian.org/debian/pool/main/x/xz-utils/",
        "package_name": "xz-utils_5.2.4-1+deb10u1_amd64.deb",
        "product": "xz",
        "version": "5.2.4",
    },
    {
        "url": "http://ftp.debian.org/debian/pool/main/x/xz-utils/",
        "package_name": "liblzma5_5.6.3-1+b1_arm64.deb",
        "product": "xz",
        "version": "5.6.3",
    },
    {
        "url": "https://downloads.openwrt.org/releases/packages-19.07/x86_64/packages/",
        "package_name": "xz_5.2.5-1_x86_64.ipk",
        "product": "xz",
        "version": "5.2.5",
    },
    {
        "url": "https://downloads.openwrt.org/releases/packages-19.07/x86_64/packages/",
        "package_name": "liblzma_5.2.5-1_x86_64.ipk",
        "product": "xz",
        "version": "5.2.5",
    },
    {
        "url": "https://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/",
        "package_name": "xz-5.2.4-r0.apk",
        "product": "xz",
        "version": "5.2.4",
        "other_products": ["gcc"],
    },
]
