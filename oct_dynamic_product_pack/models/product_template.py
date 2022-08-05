from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning
import logging

_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_pack = fields.Boolean(string="Is a Pack", default=False)
    oct_pack_price = fields.Float('Pack price', related='list_price')
    oct_pack_size = fields.Integer(string="Pack size")
    oct_product_group = fields.Many2one('oct.product.group', string='Group')
    oct_product_groups = fields.Many2many('oct.product.group', string='Groups')
    oct_qty = fields.Char(string='Qty per group')
    oct_link_ref = fields.Char(string='Link to pack', help='Link to reference the pack in website', compute='_compute_pack_link_ref')

    def _compute_pack_link_ref(self):
        for template in self:
            if template.is_pack:
                template.oct_link_ref = '/product_pack/' + str(template.id)
            else:
                template.oct_link_ref = False

    @api.model_create_multi
    def create(self, vals_list):
        templates = super(ProductTemplate, self).create(vals_list)
        for template in templates:
            if template.is_pack and len(template.oct_product_groups) == 1:
                raise UserError(_('Pack need at least two groups.'))
        return templates

    def write(self, vals):
        res = super().write(vals)
        if self.is_pack and len(self.oct_product_groups) == 1:
            raise UserError(_('Pack need at least two groups.'))
        return res
