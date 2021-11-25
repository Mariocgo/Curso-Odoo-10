# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from logging import error
from odoo import api, fields, models
from odoo.exceptions import UserError


class AccountMoveCursoLine(models.Model):
    _name = 'account.move.curso.line'
    _description = 'Participantes del curso'

    curso_id = fields.Many2one('account.move.curso', string="Curso")
    partner_id = fields.Many2one('res.partner', string="Participantes")
    vat = fields.Char(related = 'partner_id.vat')