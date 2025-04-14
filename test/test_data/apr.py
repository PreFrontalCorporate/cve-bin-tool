# Copyright (C) 2025 Orange
# SPDX-License-Identifier: GPL-3.0-or-later

mapping_test_data = [
    {
        "product": "portable_runtime",
        "version": "1.6.5",
        "version_strings": ["apr_initialize\n1.6.5"],
    }
]
package_test_data = [
    {
        "url": "http://rpmfind.net/linux/fedora/linux/development/rawhide/Everything/aarch64/os/Packages/a/",
        "package_name": "apr-1.7.5-2.fc42.aarch64.rpm",
        "product": "portable_runtime",
        "version": "1.7.5",
    },
    {
        "url": "http://ftp.debian.org/debian/pool/main/a/apr/",
        "package_name": "libapr1_1.6.5-1+b1_amd64.deb",
        "product": "portable_runtime",
        "version": "1.6.5",
    },
    {
        "url": "https://downloads.openwrt.org/releases/packages-19.07/x86_64/packages/",
        "package_name": "libapr_1.7.0-2_x86_64.ipk",
        "product": "portable_runtime",
        "version": "1.7.0",
    },
    {
        "url": "https://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/",
        "package_name": "apr-1.7.0-r0.apk",
        "product": "portable_runtime",
        "version": "1.7.0",
        "other_products": ["gcc"],
    },
]
