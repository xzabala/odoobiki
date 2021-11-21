# -*- coding: utf-8 -*-
{
    'name': "biki",
    'application':True,

    'summary': """
        Biki digitalarentzat erabilgarria den jatorrizko sistemaren informazioa kudeatzeko aplikazioa""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Uni Eibar-Ermua",
    'website': "https://www.uni.eus",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/biki_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/biki_view.xml',
        'views/biki_egoera_view.xml',
        'views/biki_emaitza_view.xml',
        'views/biki_lagina_view.xml',
        'views/biki_programa_view.xml',
        'views/biki_totala_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
