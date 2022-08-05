odoo.define('oct_dynamic_product_pack.pack_builder', function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');
    const {qweb} = require('web.core');

    publicWidget.registry.packBuilder = publicWidget.Widget.extend({
        selector: '.oct-pack-container',
        events: {
            'click .o_add_to_pack': '_onAddToPackClick',
            'click .o_remove_from_pack': '_onRemoveFromPackClick',
        },
        xmlDependencies: ["/oct_dynamic_product_pack/static/src/xml/pack_item_card.xml"],
        /**
         * @override
         */
        start: function () {
            this._super.apply(this, arguments);
            // initialize some values
            this.$packSize = this.$el.find('#pack-size').data('pack-size');
            this.$groupQty = this.$el.find('#group-qty').data('group-qty');
            this.$groupInfo = this.$el.find('#group-info').data('group-info');
            this.$packItem = this.$el.find('.oct-pack-item');
            this.$addToCart = this.$el.find('#add_to_cart');
            this.$addToCart.addClass('pack-incomplete');
        },
        _onAddToPackClick: function (ev) {
            ev.preventDefault();
            var self = this;
            var current_btn = $(ev.currentTarget);
            var product_id = current_btn.data('product-id');
            var rpcProductData = {
                route: "/search/pack_item",
                params: {
                    domain: [["id", "=", product_id]],
                },
            };
            // obtain product data and place it on pack item
            self._rpc(rpcProductData).then(function (data) {
                var product_obj = data.length > 0 ? data : null
                if (product_obj != null) {
                    for (var i = 0; i < self.$packItem.length; i++) {
                        if (self.$packItem[i].childElementCount == 0) {
                            // var $div_item = "<div class='oct-pack-iten-full'>" + product_obj[0].name + "<a href='#' class='btn btn-primary o_remove_from_pack' data-group-id='" + product_obj[0].oct_product_group + "'" + " data-product-id='" + product_obj[0].id + "'" + ">Remove</a></div>";
                            self.$packItem[i].innerHTML = qweb.render('oct_dynamic_product_pack.productPackCard', {'product': product_obj.records[0]});
                            self._onRpcCall();
                            return true;
                        }
                    }
                }
            });
        },
        _onRemoveFromPackClick: function (ev) {
            ev.preventDefault();
            var self = this;
            var item_flag = 0;
            var pack_status = $('#pack_status');
            var current_target = $(ev.currentTarget.parentNode);
            if (current_target) {
                current_target.empty();
                current_target.remove();
            }
            for (var j = 0; j < this.$packItem.length; j++) {
                if (this.$packItem[j].childNodes.length > 0) {
                    item_flag++;
                }
                if (item_flag != this.$packSize) {
                    // pack incompleto
                    this.$addToCart.addClass('pack-incomplete');
                    pack_status.addClass('d-none');
                }
            }
        },
        _countGroup: function (group, id) {
            var group_name = [];
            var group_ids = [];
            for (var i = 0; i < group.length; i++) {
                group_name.push(group[i].split(',')[1]);
                group_ids.push(parseInt(group[i].split(',')[0]));
            }
            const countOccurrences = (arr, val) => arr.reduce((a, v) => (v === val ? a + 1 : a), 0);
            var count = countOccurrences(group_ids, id);
            return count
        },
        _onRpcCall: function () {
            var item_flag = 0;
            var pack_items = $('div.oct-pack-item').find('.o_remove_from_pack');
            var pack_status = $('#pack_status');
            var group_split = this.$groupQty.split(",");
            var groups_filled = [];
            var curret_group = [];
            var group_item_count = [];

            for (var j = 0; j < pack_items.length; j++) {
                if (pack_items[j].childNodes.length > 0) {
                    curret_group = pack_items[j].attributes.getNamedItem("data-group-id").value;
                    groups_filled.push(curret_group);
                    item_flag++;
                }
                if (item_flag == this.$packSize) {
                    for (var k = 0; k < this.$groupInfo.length; k++) {
                        // count groups items
                        group_item_count.push(this._countGroup(groups_filled, this.$groupInfo[k]).toString());
                    }
                    if (JSON.stringify(group_item_count) === JSON.stringify(group_split)) {
                        // pack completo
                        this.$addToCart.removeClass('pack-incomplete');
                        pack_status.removeClass('d-none');
                    }
                    // FIXME do a else here when pack is full but not ready
                }
            }
        },
    });

});