# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class ResAccountInvoice(models.Model):
    _inherit = 'account.invoice'
    curso_id = fields.Many2one('acount.move.curso',string="Curso Asociado",readonly=True)
 

