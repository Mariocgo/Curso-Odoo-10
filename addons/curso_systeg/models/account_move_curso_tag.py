# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from logging import error
from odoo import api, fields, models
from odoo.exceptions import UserError


class AccountMoveCursoTag(models.Model):
    _name = 'account.move.curso.tag'
    # Siempre ponerle un _description a una tabla, o sale una warning
    _description = u'Clasificación del curso' 

    name = fields.Char(string="Nombre Categoria")
