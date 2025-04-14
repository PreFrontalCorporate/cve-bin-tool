# Copyright (C) 2025 Orange
# SPDX-License-Identifier: GPL-3.0-or-later

mapping_test_data = [
    {"product": "libyang", "version": "0.16", "version_strings": ["libyang-0.16"]}
]
package_test_data = [
    {
        "url": "http://rpmfind.net/linux/fedora/linux/development/rawhide/Everything/aarch64/os/Packages/l/",
        "package_name": "libyang-2.1.148-3.fc42.aarch64.rpm",
        "product": "libyang",
        "version": "2.1.148",
    },
    {
        "url": "http://ftp.debian.org/debian/pool/main/liby/libyang/",
        "package_name": "libyang0.16_0.16.105-1+deb10u1_amd64.deb",
        "product": "libyang",
        "version": "0.16.105",
    },
    {
        "url": "http://ftp.debian.org/debian/pool/main/liby/libyang/",
        "package_name": "libyang3_3.7.8-1_arm64.deb",
        "product": "libyang",
        "version": "3.7.8",
    },
    {
        "url": "https://downloads.openwrt.org/releases/packages-19.07/x86_64/packages/",
        "package_name": "libyang_0.16-r3-4_x86_64.ipk",
        "product": "libyang",
        "version": "0.16",
    },
    {
        "url": "https://dl-cdn.alpinelinux.org/alpine/v3.16/community/x86/",
        "package_name": "libyang-2.0.194-r0.apk",
        "product": "libyang",
        "version": "2.0.194",
        "other_products": ["gcc"],
    },
]
