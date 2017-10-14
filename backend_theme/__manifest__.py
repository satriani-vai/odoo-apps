# -*- coding: utf-8 -*-
"""Module information"""
# Copyright 2016, 2017 Openworx
# Copyright 2017 Hugo Rodrigues
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
# pylint: disable=pointless-statement

{
    "name": "Material/United Backend Theme",
    "summary": "Odoo 11.0 community backend theme",
    "version": "11.0.1.0.0",
    "category": "Themes/Backend",
    "website": "https://hugorodrigues.net",
    "description": """
        Backend theme for Odoo 11.0 community edition.
        """,
    "images": [
        "images/screen.png"
    ],
    "author": "Openworx, Hugo Rodrigues",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        'web_responsive',
    ],
    "excludes": [
        'web_enterprise'
    ],
    "data": [
        'views/assets.xml',
    ],
}
