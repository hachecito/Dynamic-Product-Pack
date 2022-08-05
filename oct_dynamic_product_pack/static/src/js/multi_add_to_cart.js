odoo.define('oct_dynamic_product_pack.multi_add_to_cart', function (require) {
    'use strict';

    const publicWidget = require('web.public.widget');
    const ajax = require('web.ajax');
    require('website_sale.website_sale');
    require('website_sale_stock.VariantMixin');

    publicWidget.registry.WebsiteSale.include({
        /**
         * @override
         */
        _onClickAdd(ev) {
            this._super.apply(this, arguments).then(() => {
                ev.preventDefault();
                var pack_items = $('div.oct-pack-item').find('.o_remove_from_pack');
                var from_pack = $('input#from-pack').data('from-pack');
                var pack_size = $('input#pack-size').data('pack-size');
                var items_filled = [];

                if (pack_size) {
                    for (var i = 0; i < pack_items.length; i++) {
                        items_filled.push(pack_items[i].attributes.getNamedItem("data-product-id").value);
                    }
                }

                if (items_filled.length == pack_size) {
                    ajax.jsonRpc('/add_to_cart/extra_products/', 'call', {'data': items_filled, 'from_pack': from_pack }).then(function (data) {
                            setTimeout(() => {
                                console.log(data);
                                $('header sup.my_cart_quantity').text(data);
                            }, 1000);
                        },
                    )
                }
            });
        }
    });
});
