# Copyright (C) 2025 Orange
# SPDX-License-Identifier: GPL-3.0-or-later

mapping_test_data = [
    {
        "product": "cups-filters",
        "version": "1.21.6",
        "version_strings": ["cups-filters version 1.21.6"],
    }
]
package_test_data = [
    {
        "url": "http://rpmfind.net/linux/fedora/linux/development/rawhide/Everything/aarch64/os/Packages/c/",
        "package_name": "cups-filters-2.0.1-3.fc43.aarch64.rpm",
        "product": "cups-filters",
        "version": "2.0.1",
    },
    {
        "url": "http://ftp.debian.org/debian/pool/main/c/cups-filters/",
        "package_name": "cups-filters_1.21.6-5_amd64.deb",
        "product": "cups-filters",
        "version": "1.21.6",
    },
    {
        "url": "https://dl-cdn.alpinelinux.org/alpine/v3.11/community/x86_64/",
        "package_name": "cups-filters-1.26.0-r0.apk",
        "product": "cups-filters",
        "version": "1.26.0",
        "other_products": ["gcc"],
    },
]
