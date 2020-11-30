# -*- coding: utf-8 -*-
{
    'name': "Sale",
    'summary': """This module will add extra field in sale line""",
    'description': """This module will add extra field in sale line""",
    'author': "Aktiv software",
    'website': "http://www.aktivesoftware.com",
    'category': 'Tools',
    'version': '13.0.1.0.0',
    'depends': ['base', 'sale_management',
                'sale', ],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_views.xml',
        'views/account_move_views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
