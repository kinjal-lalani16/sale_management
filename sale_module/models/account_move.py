from odoo import fields, models

class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    sale_id = fields.Many2one('sale.order.line', string="Sale")
    sale_ids = fields.Many2many('sale.order', 'sale_move', 'sale_id', 'sale_name', string="Order")
