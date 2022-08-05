from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ProductGroup(models.Model):
    _name = "oct.product.group"
    _description = "Analytic distribution"
    _order = "id asc"

    name = fields.Char()
    oct_product_group = fields.Many2many("product.template", string="Products")
    oct_products = fields.One2many('product.template', 'oct_product_group', string='Products')
