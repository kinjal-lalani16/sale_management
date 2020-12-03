from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    sale_id = fields.Many2one('sale.order.line', string="Sale")
    sale_ids = fields.Many2many('sale.order', string="Order")

    def _prepare_invoice_line(self):
        res = super(SaleOrderLine, self)._prepare_invoice_line()
        print('\n\n\n----------res----------\n\n\n', res)
        res['sale_id'] = self.sale_id.id
        lst = []
        for move in self:
            for line in move.sale_ids:
                lst.append((1, line.id, {'sale_ids': self.sale_ids}))
        res['sale_ids'] = lst
        print('\n\n\n----------res----------\n\n\n', res)
        return res


    def _prepare_procurement_values(self, group_id=False):
        fields = super(SaleOrderLine, self)._prepare_procurement_values(group_id)
        print('\n\n\n-----sale_id-----\n\n', self.sale_id)
        fields.update({
            'sale_id': self.sale_id,
        })
        return fields


    @api.onchange('product_id')
    def product_id_change(self):
        super(SaleOrderLine, self).product_id_change()
        sale_list = []
        for sale in self.product_id.sale_ids:
            sale_list.append(sale.id)
        self.update({'sale_ids': [(6, 0, sale_list)]})

class StockRule(models.Model):
    _inherit = "stock.rule"

    def _get_stock_move_values(self, product_id, product_qty, product_uom, location_id, name, origin, company_id, values):
        print('\n\n-----first-----\n\n')
        result = super(StockRule, self)._get_stock_move_values(product_id, product_qty, product_uom, location_id, name, origin, company_id, values)
        result['sale_id'] = self.env['sale.order.line'].browse(values['sale_line_id']).sale_id.id
        return result
