# ╔══════════════════════════════════════════════════════════════════════╗
# ║           ___     ____   _____   _   _   ____    _   _   ____        ║
# ║          / _ \   / ___| |_   _| | | | | |  _ \  | | | | / ___|       ║
# ║         | | | | | |       | |   | | | | | |_) | | | | | \___ \       ║
# ║         | |_| | | |___    | |   | |_| | |  __/  | |_| |  ___) |      ║
# ║          \___/   \____|   |_|    \___/  |_|      \___/  |____/       ║
# ║                                                                      ║
# ║                       OCTUPUS TECHNOLOGIES S.L                       ║
# ║                 C/ Albasanz, 52 28037 Madrid, España                 ║
# ║                             +34 687542055                            ║
# ║                        jvalladolid@octupus.es                        ║
# ║                        https://www.octupus.es                        ║
# ║                                                                      ║
# ╚══════════════════════════════════════════════════════════════════════╝
{
    'name': "OCT Dynamic Product Pack",

    'summary': "OCT Dynamic Product Pack",

    'author': "Yhasmani Valdes Migenes, Octupus Technologies S.L.",
    'website': "https://www.octupus.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': "eCommerce",
    'version': '15.0.2.0.1',

    'depends': ['website', 'website_sale', 'stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_view.xml',
        'views/product_group_view.xml',
        'views/templates.xml',
    ],
    # assets
    'assets': {
        'web.assets_frontend': [
            'oct_dynamic_product_pack/static/src/scss/oct_style.scss',
            'oct_dynamic_product_pack/static/src/js/pack_builder.js',
            'oct_dynamic_product_pack/static/src/js/multi_add_to_cart.js',
            'oct_dynamic_product_pack/static/src/js/multi_remove_from_cart.js',
        ],
    },
    'license': "LGPL-3",
}
