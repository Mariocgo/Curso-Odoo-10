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
        ],
    'description': """
Module for defining analytic accounting object.
===============================================
    El primer modulazo
    """,
    'data': [
        'security/security.xml', #agrega los grupos para poder usarlo en el siguiente archivo
        'security/ir.model.access.csv', #Necesita los grupos creados en el archivo anterior
        'views/account_move_curso_view.xml',
        'views/res_partner_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
