# Copyright (C) 2021 Intel Corporation
# SPDX-License-Identifier: GPL-3.0-or-later

mapping_test_data = [
    {
        "product": "strongswan",
        "version": "4.6.3",
        "version_strings": ["(strongSwan 4.6.3"],
    }
]
package_test_data = [
    {
        "url": "https://kojipkgs.fedoraproject.org/packages/strongswan/4.6.2/1.fc16/x86_64/",
        "package_name": "strongswan-4.6.2-1.fc16.x86_64.rpm",
        "product": "strongswan",
        "version": "4.6.2",
    },
    {
        "url": "http://ftp.debian.org/debian/pool/main/s/strongswan/",
        "package_name": "strongswan-charon_5.7.2-1+deb10u2_amd64.deb",
        "product": "strongswan",
        "version": "5.7.2",
    },
    {
        "url": "https://downloads.openwrt.org/releases/packages-19.07/x86_64/packages/",
        "package_name": "strongswan-charon_5.8.2-2_x86_64.ipk",
        "product": "strongswan",
        "version": "5.8.2",
    },
    {
        "url": "https://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/",
        "package_name": "strongswan-5.8.1-r2.apk",
        "product": "strongswan",
        "version": "5.8.1",
        "other_products": ["gcc"],
    },
]
