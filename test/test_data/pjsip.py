# Copyright (C) 2025 Orange
# SPDX-License-Identifier: GPL-3.0-or-later

mapping_test_data = [
    {"product": "pjsip", "version": "2.9", "version_strings": ["PJ_ESOCKETSTOP)\n2.9"]}
]
package_test_data = [
    {
        "url": "http://rpmfind.net/linux/fedora/linux/development/rawhide/Everything/aarch64/os/Packages/p/",
        "package_name": "pjproject-2.13.1-6.fc42.aarch64.rpm",
        "product": "pjsip",
        "version": "2.13.1",
        "other_products": ["libsrtp"],
    },
    {
        "url": "https://downloads.openwrt.org/releases/packages-19.07/x86_64/telephony/",
        "package_name": "libpj_2.10-3_x86_64.ipk",
        "product": "pjsip",
        "version": "2.10",
    },
    {
        "url": "https://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/",
        "package_name": "pjproject-2.9-r0.apk",
        "product": "pjsip",
        "version": "2.9",
        "other_products": ["gcc"],
    },
]
