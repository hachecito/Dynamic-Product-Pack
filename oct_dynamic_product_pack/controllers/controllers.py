import logging
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo import fields, http, tools

_logger = logging.getLogger(__name__)


class OctWebsiteSale(WebsiteSale):

    @http.route(['/shop/cart/update_json'], type='json', auth="public", methods=['POST'], website=True, csrf=False)
    def cart_update_json(self, product_id, line_id=None, add_qty=None, set_qty=None, display=True, **kw):
        record = super().cart_update_json(
            product_id=product_id,
            line_id=line_id,
            add_qty=add_qty,
            set_qty=set_qty,
            display=display,
            kw=kw
        )
        # order = request.website.sale_get_order()
        # linked_line_id = order.order_line.browse(int(record['line_id']))
        # FIXME maybe will use it on future

        return record

    @http.route(['/add_to_cart/extra_products/'], type='json', auth="public", methods=['POST'], website=True)
    def cart_update_multi_extra_products(self, data, from_pack):
        product_tmpl = 0
        cart_data = {}
        product_tmpl_model = request.env['product.template']
        order = request.website.sale_get_order(force_create=True)
        product_tmpl_from = product_tmpl_model.browse(int(from_pack))
        for i in range(len(data)):
            product_tmpl = product_tmpl_model.browse(int(data[i]))
            first = product_tmpl.sudo()._get_first_possible_variant_id()
            # get line in order that match with pack item
            order_line = order._cart_find_product_line(product_id=first, from_def=True, from_pack=product_tmpl_from)[:1]
            if order_line:
                cart_data = self.cart_update_json(product_id=first, line_id=order_line.id, add_qty=1)
            else:
                cart_data = self.cart_update_json(product_id=first, line_id=False, add_qty=1)
            if cart_data['line_id']:
                order.order_line.browse(int(cart_data['line_id'])).update({'from_pack': product_tmpl_from})
                order.order_line.browse(int(cart_data['line_id'])).update({'price_unit': 0.0})

        result = order.cart_quantity
        return result


class ProductPack(http.Controller):

    @http.route(['/product_pack/<int:pack_id>'], type='http', auth='public', website=True)
    def get_all_packs(self, pack_id):
        packs = request.env['product.template'].sudo().search([('is_pack', '=', True)])
        # only show package defined in url
        packs = packs.browse(pack_id)
        grouped_pack = {}
        pack_groups = []
        if packs and packs.oct_product_groups:
            # update list with all the different groups
            grouped_pack.update((g.name, []) for g in packs.oct_product_groups)
            pack_groups = [p.id for p in packs.oct_product_groups]
            for group in packs.oct_product_groups:
                if group.oct_products:
                    for product in group.oct_products:
                        # add product to corresponding group.
                        grouped_pack[group.name].append(product)
        return request.render('oct_dynamic_product_pack.oct_pack_ecommerce_page',
                              {'packs': packs, 'grouped_pack': grouped_pack, 'pack_groups': pack_groups})

    @http.route(['/sale_order/pack_lines'], type='json', auth="public", methods=['POST'], website=True)
    def cart_update_multi_extra_products(self, product_id):
        product = request.env['product.product'].sudo().browse(int(product_id))
        order = request.website.sale_get_order()
        if product.is_pack:
            for line in order.order_line:
                if line.from_pack and line.from_pack.id == product.product_tmpl_id.id:
                    line.sudo().unlink()
                # if line.product_id.id == product.id:
                #     line.unlink()
            return True
        else:
            return False

    @http.route(['/search/pack_item'], type='json', auth="public", methods=['POST'], website=True)
    def search_pack_item(self, domain):
        records = request.env['product.template'].sudo().search_read(domain)
        length = len(records)
        if not records:
            return {
                'length': 0,
                'records': []
            }
        return {
            'length': length,
            'records': records
        }
