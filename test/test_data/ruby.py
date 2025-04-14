# Copyright (C) 2025 Orange
# SPDX-License-Identifier: GPL-3.0-or-later

mapping_test_data = [
    {"product": "ruby", "version": "2.6.8", "version_strings": ["ruby 2.6.8"]}
]
package_test_data = [
    {
        "url": "http://rpmfind.net/linux/fedora/linux/development/rawhide/Everything/aarch64/os/Packages/r/",
        "package_name": "ruby-libs-3.4.2-23.fc43.aarch64.rpm",
        "product": "ruby",
        "version": "3.4.2",
        "other_products": ["rust"],
    },
    {
        "url": "http://ftp.debian.org/debian/pool/main/r/ruby2.5/",
        "package_name": "libruby2.5_2.5.5-3+deb10u4_amd64.deb",
        "product": "ruby",
        "version": "2.5.5",
    },
    {
        "url": "https://downloads.openwrt.org/releases/packages-19.07/x86_64/packages/",
        "package_name": "libruby2.6_2.6.10-1_x86_64.ipk",
        "product": "ruby",
        "version": "2.6.10",
    },
    {
        "url": "https://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/",
        "package_name": "ruby-libs-2.6.8-r0.apk",
        "product": "ruby",
        "version": "2.6.8",
        "other_products": ["gcc"],
    },
]
