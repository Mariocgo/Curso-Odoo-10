# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class ResUser(models.Model):
    _inherit = 'res.users'
    is_responsable = fields.Boolean(string="Usuario responsable")
