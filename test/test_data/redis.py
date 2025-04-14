# Copyright (C) 2025 Orange
# SPDX-License-Identifier: GPL-3.0-or-later

mapping_test_data = [
    {
        "product": "redis",
        "version": "5.0.14",
        "version_strings": ["5.0.14\nredis_version"],
    }
]
package_test_data = [
    {
        "url": "http://rpmfind.net/linux/fedora/linux/updates/40/Everything/aarch64/Packages/r/",
        "package_name": "redis-7.2.7-1.fc40.aarch64.rpm",
        "product": "redis",
        "version": "7.2.7",
        "other_products": ["lua"],
    },
    {
        "url": "http://ftp.debian.org/debian/pool/main/r/redis/",
        "package_name": "redis-tools_5.0.14-1+deb10u2_amd64.deb",
        "product": "redis",
        "version": "5.0.14",
    },
    {
        "url": "https://downloads.openwrt.org/releases/packages-21.02/x86_64/packages/",
        "package_name": "redis-server_6.2.6-1_x86_64.ipk",
        "product": "redis",
        "version": "6.2.6",
        "other_products": ["lua"],
    },
    {
        "url": "https://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/",
        "package_name": "redis-5.0.14-r0.apk",
        "product": "redis",
        "version": "5.0.14",
        "other_products": ["gcc", "lua"],
    },
]
