from odoo import fields, models

class StockMove(models.Model):
    _inherit = 'stock.move'

    sale_id = fields.Many2one('sale.order.line', string="Sale")


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    sale_id = fields.Many2one('sale.order.line', string="Sale")
