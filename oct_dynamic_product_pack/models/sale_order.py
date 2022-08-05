from odoo import models, fields, api, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    from_pack = fields.Many2one('product.template', string='From Pack')
    pack_items = fields.Many2many('product.template', string='Pack Items')


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _cart_find_product_line(self, product_id=None, line_id=None, **kwargs):
        self.ensure_one()
        lines = super(SaleOrder, self)._cart_find_product_line(product_id, line_id)
        product = self.env['product.product'].browse(product_id)
        order = self.sudo().browse(self.id)
        pack_line = []
        for pack in order.order_line:
            if pack.product_id.is_pack:
                pack_line.append(pack.product_id.product_tmpl_id)
        if line_id:
            return lines
        if kwargs.get('from_def') and kwargs.get('from_pack'):
            return lines.filtered(lambda l: l.from_pack and l.from_pack == kwargs.get('from_pack'))

        return lines.filtered(lambda l: not l.from_pack)
