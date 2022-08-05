odoo.define('oct_dynamic_product_pack.multi_remove_from_cart', function (require) {
    'use strict';

    const publicWidget = require('web.public.widget');
    const ajax = require('web.ajax');
    require('website_sale.website_sale');
    require('website_sale_stock.VariantMixin');

    publicWidget.registry.websiteSaleCart.include({
        /**
         * @override
         */
        _onClickDeleteProduct(ev) {
            ev.preventDefault();
            var current_product = $(ev.currentTarget).closest('tr').find('.js_quantity').data('product-id');
            ajax.jsonRpc('/sale_order/pack_lines', 'call', {'product_id': current_product}).then(function (data) {
                $(ev.currentTarget).closest('tr').find('.js_quantity').val(0).trigger('change');
            })
        }
    });
});
