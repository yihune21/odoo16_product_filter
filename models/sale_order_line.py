from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.model
    def _product_domain(self):
        return [
            ('sale_ok', '=', True),
            ('type', 'in', ['consu', 'product', 'service'])
        ]

    product_id = fields.Many2one(
        'product.product', string='Product',
        domain=_product_domain,
        change_default=True, ondelete='restrict')