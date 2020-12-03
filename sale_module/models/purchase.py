from odoo import api, fields, models

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    sale_ids = fields.Many2many('sale.order', 'sale_table', 'sale_id', 'sale_name', string="Sale")

    @api.onchange('product_id')
    def onchange_product_id(self):
        super(PurchaseOrderLine, self).onchange_product_id()
        sale_list = []
        for sale in self.product_id.sale_ids:
            sale_list.append(sale.id)
        self.write({'sale_ids': [(6, 0, sale_list)]})
