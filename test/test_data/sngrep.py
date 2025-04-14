# Copyright (C) 2023 Orange
# SPDX-License-Identifier: GPL-3.0-or-later

mapping_test_data = [
    {"product": "sngrep", "version": "1.4.6", "version_strings": ["sngrep\n1.4.6"]}
]
package_test_data = [
    {
        "url": "http://rpmfind.net/linux/opensuse/ports/i586/tumbleweed/repo/oss/i586/",
        "package_name": "sngrep-1.7.0-1.2.i586.rpm",
        "product": "sngrep",
        "version": "1.7.0",
    },
    {
        "url": "http://ftp.debian.org/debian/pool/main/s/sngrep/",
        "package_name": "sngrep_1.4.6-1_amd64.deb",
        "product": "sngrep",
        "version": "1.4.6",
    },
    {
        "url": "https://downloads.openwrt.org/releases/packages-19.07/x86_64/telephony/",
        "package_name": "sngrep_1.4.6-1_x86_64.ipk",
        "product": "sngrep",
        "version": "1.4.6",
    },
    {
        "url": "https://dl-cdn.alpinelinux.org/alpine/v3.20/community/x86/",
        "package_name": "sngrep-1.8.1-r0.apk",
        "product": "sngrep",
        "version": "1.8.1",
        "other_products": ["gcc"],
    },
]
