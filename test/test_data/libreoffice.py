# Copyright (C) 2025 Orange
# SPDX-License-Identifier: GPL-3.0-or-later

mapping_test_data = [
    {
        "product": "libreoffice",
        "version": "6.1.5",
        "version_strings": ["libreoffice-6.1.5"],
    }
]
package_test_data = [
    {
        "url": "http://ftp.debian.org/debian/pool/main/libr/libreoffice/",
        "package_name": "libreoffice-base-core_6.1.5-3+deb10u7_amd64.deb",
        "product": "libreoffice",
        "version": "6.1.5",
    },
    {
        "url": "https://dl-cdn.alpinelinux.org/alpine/v3.11/community/x86/",
        "package_name": "libreoffice-base-6.3.2.2-r3.apk",
        "product": "libreoffice",
        "version": "6.3.2.2",
        "other_products": ["gcc"],
    },
]
