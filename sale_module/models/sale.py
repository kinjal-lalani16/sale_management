from odoo import api, fields, models


# class SaleOrder(models.Model):
#     _inherit = "sale.order"


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    sale_id = fields.Many2one('sale.order.line', string="Sale")
    sale_ids = fields.Many2many('sale.order', string="Order")


    def _prepare_invoice_line(self):
        res = super(SaleOrderLine, self)._prepare_invoice_line()
        res['sale_id'] = self.sale_id.id
        res.update({'sale_ids': [(6, 0, self.sale_ids.ids)]})
        print('\n\n\n----------res----------\n\n\n', res)
        return res


    @api.onchange('product_id')
    def product_id_change(self):
        super(SaleOrderLine, self).product_id_change()
        sale_list = []
        for sale in self.product_id.sale_ids:
            sale_list.append(sale.id)
        self.update({'sale_ids': [(6, 0, sale_list)]})

