# Copyright (C) 2025 Orange
# SPDX-License-Identifier: GPL-3.0-or-later

mapping_test_data = [
    {
        "product": "openvswitch",
        "version": "2.11.6",
        "version_strings": ["openvswitch 2.11.6"],
    }
]
package_test_data = [
    {
        "url": "http://rpmfind.net/linux/fedora/linux/development/rawhide/Everything/aarch64/os/Packages/o/",
        "package_name": "openvswitch-3.4.1-1.fc42.aarch64.rpm",
        "product": "openvswitch",
        "version": "3.4.1",
    },
    {
        "url": "http://ftp.debian.org/debian/pool/main/o/openvswitch/",
        "package_name": "openvswitch-common_2.10.7+ds1-0+deb10u1_amd64.deb",
        "product": "openvswitch",
        "version": "2.10.7",
    },
    {
        "url": "https://downloads.openwrt.org/releases/packages-19.07/x86_64/packages/",
        "package_name": "openvswitch-libopenvswitch_2.11.6-1_x86_64.ipk",
        "product": "openvswitch",
        "version": "2.11.6",
    },
    {
        "url": "https://dl-cdn.alpinelinux.org/alpine/v3.11/community/x86_64/",
        "package_name": "openvswitch-2.12.0-r2.apk",
        "product": "openvswitch",
        "version": "2.12.0",
        "other_products": ["gcc"],
    },
]
