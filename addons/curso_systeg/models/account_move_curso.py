# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from logging import error
from odoo import api, fields, models
from odoo.exceptions import UserError


class AccountMoveCurso(models.Model):
    _name = 'account.move.curso'
    _description = 'Curso en Facturas'

    name = fields.Char(string='Nombre del curso')
    invoice_id = fields.Many2one('account.invoice',string="Factura asociada",readonly=True)
    purchase_id = fields.Many2one('purchase.order',string="Compra asociada", readonly=True)
    state = fields.Selection([
            ('draft','Borrador'),
            ('open', 'Abierto'),
            ('closed', 'Cerrado'),
        ], string='Status', index=True, readonly=True, default='draft',copy=False)
    date_init = fields.Date(string='Fecha Inicio')
    date_end = fields.Date(string='Fecha Final')
    facilitador = fields.Many2one('res.partner',string='Facilitador')
    supervisor = fields.Many2one('res.partner',string='Supervisor')
    is_responsable = fields.Many2one('res.users',string="Usuario responsable")
    duracion = fields.Integer(string="Duración")
    costo_hora = fields.Float(string="Costo de la hora")
    currency_id = fields.Many2one("res.currency",
        string="Moneda",
        default=lambda self: self.env.user.company_id.currency_id.id,
        readonly=True,
    )
    @api.depends('duracion','costo_hora')
    def _compute_costo_total(self):
        self.costo_total = 0
        if self.duracion > 0 and self.costo_hora > 0:
            self.costo_total = self.costo_hora * self.duracion

    costo_total = fields.Monetary(string="Costo Total", currency_field='currency_id', 
    compute="_compute_costo_total",store=True)
    

    def action_open(self):
        # if self.costo_total < 1000:
        #     raise UserError(("El costo del curso debe ser mayor a 1000 pelucholares,actualmente el costo es %s")%(self.costo_total))
        # if not self.purchase_id:
        #     raise UserError("Necesita asociar una compra antes de cambiar el estado del curso")
        # if len(self.participantes) == 0:
        #     raise UserError("Debes tener al menos un participante ")
        if not self.name:
            self.name = self.env['ir.sequence'].next_by_code('account.move.curso') or '/'
        self.state = "open" 
    
    participantes = fields.One2many('account.move.curso.line', 'curso_id',
        string="participantes"
    )
    categ_id = fields.Many2many('account.move.curso.tag',
        string="Categorias"
    )
    
    # @api.model
    # def create(self, vals):
        # if vals.get('name', ''):
        # vals['name'] = self.env['ir.sequence'].next_by_code('account.move.curso') or '/'
        # return super(AccountMoveCurso, self).create(vals)

