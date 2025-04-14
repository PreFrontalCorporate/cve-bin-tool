# Copyright (C) 2025 Orange
# SPDX-License-Identifier: GPL-3.0-or-later

mapping_test_data = [
    {
        "product": "gnu_sasl",
        "version": "1.10.0",
        "version_strings": ["1.10.0\nSASLprep"],
    }
]
package_test_data = [
    {
        "url": "http://rpmfind.net/linux/fedora/linux/development/rawhide/Everything/aarch64/os/Packages/l/",
        "package_name": "libgsasl-1.10.0-12.fc42.aarch64.rpm",
        "product": "gnu_sasl",
        "version": "1.10.0",
    },
    {
        "url": "http://ftp.debian.org/debian/pool/main/g/gsasl/",
        "package_name": "libgsasl7_1.10.0-4+deb11u1_amd64.deb",
        "product": "gnu_sasl",
        "version": "1.10.0",
    },
    {
        "url": "https://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/",
        "package_name": "libgsasl-1.8.1-r0.apk",
        "product": "gnu_sasl",
        "version": "1.8.1",
        "other_products": ["gcc"],
    },
]
