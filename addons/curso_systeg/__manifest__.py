# -*- coding: utf-8 -*-
{
    'name' : 'Curso',
    'version': '1.1',
    'website' : 'https://www.odoo.com/page/accounting',
    'category': 'Accounting',
    'depends' : [
        'base',
        'mail', 
        'account',
        'purchase',
        ],
    'description': """
Module for defining analytic accounting object
===============================================
    El primer modulazo
    """,
    'data': [
        'data/sequence.xml',
        'security/security.xml', #agrega los grupos para poder usarlo en el siguiente archivo
        'security/ir.model.access.csv', #Necesita los grupos creados en el archivo anterior
        'views/account_move_curso_view.xml',
        'views/res_partner_view.xml',
        'views/res_users_view.xml',
        'views/purchase_order_view.xml',
        'views/account_invoice_view.xml',
        'views/account_move_curso_tag_view.xml',
        'report/report_Account_move_curso.xml',
        'report/report_Purchase_order.xml',

    ],
    'installable': True,
    'auto_install': False,
}
