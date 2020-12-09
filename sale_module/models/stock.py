from odoo import fields, models

class StockMove(models.Model):
    _inherit = 'stock.move'

    sale_id = fields.Many2one('sale.order.line', string="Sale")
    sale_ids = fields.Many2many('sale.order', 'sale_order_ref', 'sale_id', 'sale_name',string='Order')


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    sale_id = fields.Many2one('sale.order.line', string="Sale")
    sale_ids = fields.Many2many('sale.order', 'sale_order_ref_stock', 'sale_id', 'sale_name',string='Order')

class StockRule(models.Model):
    _inherit = "stock.rule"

    def _get_stock_move_values(self, product_id, product_qty, product_uom, location_id, name, origin, company_id, values):
        print('\n\n-----first-----\n\n', values)
        result = super(StockRule, self)._get_stock_move_values(product_id, product_qty, product_uom, location_id, name, origin, company_id, values)
        result['sale_id'] = self.env['sale.order.line'].browse(values['sale_line_id']).sale_id.id
        result.update({
            'sale_ids': [(4, s.id) for s in self.env['sale.order.line'].browse(
                values['sale_line_id']).sale_ids]
        })
        # result['sale_ids'] = self.env['sale.order.line'].browse(values['sale_line_id']).sale_ids.ids

        print('\n\n-----result----\n\n', result)

        return result
