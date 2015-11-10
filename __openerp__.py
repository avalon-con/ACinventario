# -*- coding: utf-8 -*-
{
    'name': "Avalon - Inventario",
    'summary': """
        Inventario y Almacenes""",
    'description': """
    Descripción Larga
    """,
    'author': "Avalon Consultores C.A.",
    'website': "http://www.avalon.com/inventario",
    'category': 'Inventory',
    'version': '0.1',
    'license': 'AGPL-3',
    'depends': ['base','stock','mail'],
    'data': [
        # 'security/ir.model.access.csv',
        'views.xml',
        'templates.xml',
    ],
    'demo': [
        'demo.xml',
    ],
}