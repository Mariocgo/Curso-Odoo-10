# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ResPurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    curso_id = fields.Many2one('account.move.curso',string="Curso Asociado")

    def button_confirm(self):       
        res =  super(ResPurchaseOrder, self).button_confirm()
        if self.curso_id:
            self.curso_id.purchase_id=self.id
        return res

 

