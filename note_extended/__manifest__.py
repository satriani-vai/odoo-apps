# -*- coding: utf-8 -*-
{
    'name': 'Notes Extended',
    'version': '10.0.1.0',
    'description': """Adds extra functionality to Odoo Notes""",
    'summary': 'Auto archive notes',
    'author': 'Hugo Rodrigues',
    'website': 'https://hugorodrigues.net',
    'license': 'Other OSI approved licence',
    'category': 'Tools',
    'depends': [
        'note',
    ],
    'data': [
        'views/note_views.xml'
    ],
    'installable': True,
    'application': True,
    'auto_instal': False
}
