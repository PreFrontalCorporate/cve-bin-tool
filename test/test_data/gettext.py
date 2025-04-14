# Copyright (C) 2025 Keysight Technologies
# SPDX-License-Identifier: GPL-3.0-or-later

mapping_test_data = [
    {
        "product": "gettext",
        "version": "0.19.8.1",
        "version_strings": [
            "../../../gettext-0.19.8.1/gettext-tools/gnulib-lib/mbiter.h"
        ],
    },
    {
        "product": "gettext",
        "version": "0.22.3",
        "version_strings": [
            "/usr/src/gettext/gettext-0.22.3-1.x86_64/src/gettext-0.22.3/gettext-tools/libgettextpo/../src/format-kde-kuit.c"
        ],
    },
]
package_test_data = [
    {
        "url": "https://ftp-stud.hs-esslingen.de/pub/Mirrors/sources.redhat.com/cygwin/x86_64/release/gettext/libgettextpo0/",
        "package_name": "libgettextpo0-0.22.3-1.tar.xz",
        "product": "gettext",
        "version": "0.22.3",
        "other_products": ["gcc"],
    },
    {
        "url": "http://rpmfind.net/linux/fedora/linux/development/rawhide/Everything/aarch64/os/Packages/g/",
        "package_name": "gettext-0.23.1-2.fc42.aarch64.rpm",
        "product": "gettext",
        "version": "0.23.1",
    },
    {
        "url": "http://ftp.debian.org/debian/pool/main/g/gettext/",
        "package_name": "gettext_0.19.8.1-9_amd64.deb",
        "product": "gettext",
        "version": "0.19.8.1",
    },
    {
        "url": "https://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/",
        "package_name": "gettext-0.20.1-r2.apk",
        "product": "gettext",
        "version": "0.20.1",
        "other_products": ["gcc"],
    },
]
