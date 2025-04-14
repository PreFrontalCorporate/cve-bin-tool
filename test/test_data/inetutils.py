# Copyright (C) 2025 Orange
# SPDX-License-Identifier: GPL-3.0-or-later

mapping_test_data = [
    {
        "product": "inetutils",
        "version": "1.9.4",
        "version_strings": ["1.9.4\nGNU inetutils"],
    }
]
package_test_data = [
    {
        "url": "http://ftp.debian.org/debian/pool/main/i/inetutils/",
        "package_name": "inetutils-ftp_1.9.4-7+deb10u1_amd64.deb",
        "product": "inetutils",
        "version": "1.9.4",
    },
    {
        "url": "http://ftp.debian.org/debian/pool/main/i/inetutils/",
        "package_name": "inetutils-telnetd_2.5-5_amd64.deb",
        "product": "inetutils",
        "version": "2.5",
    },
    {
        "url": "https://dl-cdn.alpinelinux.org/alpine/v3.11/community/x86_64/",
        "package_name": "inetutils-syslogd-1.9.4-r3.apk",
        "product": "inetutils",
        "version": "1.9.4",
        "other_products": ["gcc"],
    },
]
