from odoo import fields, models

class ProductProduct(models.Model):
    _inherit = 'product.template'

    sale_ids = fields.Many2many('sale.order', 'sale_order_rel', 'sale_id', 'product_id', string="sales")
    pro = fields.Char(string="Product")
