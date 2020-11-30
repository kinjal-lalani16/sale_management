from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    sale_id = fields.Many2one('sale.order.line', string="Sale")
    # sale_id = fields.Char(string="sale")

    def _prepare_invoice_line(self):
        res = super(SaleOrderLine, self)._prepare_invoice_line()
        res['sale_id'] = self.sale_id.id
        return res
