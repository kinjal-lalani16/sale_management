from odoo import fields, models

class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    sale_id = fields.Many2one('sale.order.line', string="Sale")
