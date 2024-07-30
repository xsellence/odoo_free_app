# -*- coding: utf-8 -*-
{
    'name': "Employee Blood Group",

    'summary': "Employee Blood Group in Employee Profile.",

    'description': """
     Employee Blood Group in Employee Profile.
    """,

    'author': "Umme Huzaifa, Xsellence Bangladesh Ltd.",
    'website': "https://xsellence-bangladesh-ltd.odoo.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '17.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'images': ['static/description/banner.jpg'],
    'license': 'LGPL-3',
}

