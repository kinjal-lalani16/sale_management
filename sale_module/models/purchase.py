from odoo import api, fields, models

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    sale_id = fields.Many2one('sale.order.line', string="sale")
    sale_ids = fields.Many2many('sale.order', 'sale_table', 'sale_id', 'sale_name', string="Order")

    @api.onchange('product_id')
    def onchange_product_id(self):
        super(PurchaseOrderLine, self).onchange_product_id()
        sale_list = []
        for sale in self.product_id.sale_ids:
            sale_list.append(sale.id)
        self.write({'sale_ids': [(6, 0, sale_list)]})

    def _prepare_stock_moves(self, picking):
        res = super(PurchaseOrderLine, self)._prepare_stock_moves(picking)
        print("\n\n\n\n\n", res)
        res[0]['sale_id'] = self.sale_id.id
        res[0]['sale_ids'] = self.sale_ids.ids
        return res


    def _prepare_account_move_line(self, move):
        res = super(PurchaseOrderLine, self)._prepare_account_move_line(move)
        res['sale_id'] = self.sale_id.id
        res['sale_ids'] = self.sale_ids.ids

        return res
