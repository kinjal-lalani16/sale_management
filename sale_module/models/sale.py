from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    sale_id = fields.Many2one('sale.order.line', string="Sale")
    # sale_id = fields.Char(string="sale")

    def _prepare_invoice_line(self):
        res = super(SaleOrderLine, self)._prepare_invoice_line()
        res['sale_id'] = self.sale_id.id
        return res


    def _prepare_procurement_values(self, group_id=False):
        fields = super(SaleOrderLine, self)._prepare_procurement_values(group_id)
        print('\n\n\n-----sale_id-----\n\n', self.sale_id)
        fields.update({
            'sale_id': self.sale_id,
        })
        return fields

class StockRule(models.Model):
    _inherit = "stock.rule"

    def _get_stock_move_values(self, product_id, product_qty, product_uom, location_id, name, origin, company_id, values):
        print('\n\n-----first-----\n\n')
        result = super(StockRule, self)._get_stock_move_values(product_id, product_qty, product_uom, location_id, name, origin, company_id, values)
        result['sale_id'] = self.env['sale.order.line'].browse(values['sale_line_id']).sale_id.id
        return result
