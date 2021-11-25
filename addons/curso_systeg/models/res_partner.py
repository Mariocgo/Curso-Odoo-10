# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    is_facilitador = fields.Boolean(string="Falicitador")
    is_supervisor = fields.Boolean(string="Supervisor")

