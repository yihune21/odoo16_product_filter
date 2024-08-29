# -*- coding: utf-8 -*-
{
    'name': 'Product Filter',
    'version': '0.1',
    'summary': 'Filter products on purchase and sale order lines',
    'description': 'This module filters products that can be purchased on purchase order lines and products that can be sold on sale order lines.',
    'category': 'Sales/Purchase',
    'author': 'Yihune Zewdie',
    'depends': ['base','sale', 'purchase'],
    'data': [
        'views/purchase_view.xml',
        'views/sale_view.xml',
    ],
    'website': "https://www.yourcompany.com",
    'installable': True,
    'application': False,
     'license':'LGPL-3'
}
