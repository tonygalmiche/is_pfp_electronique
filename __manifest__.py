# -*- coding: utf-8 -*-
{
    'name'     : 'InfoSaône - Module Odoo pour CRM PFP Electronique',
    'version'  : '0.1',
    'author'   : 'InfoSaône',
    'category' : 'InfoSaône',


    'description': """
InfoSaône - Module Odoo pour CRM PFP Electronique
===================================================
""",
    'maintainer' : 'InfoSaône',
    'website'    : 'http://www.infosaone.com',
    'depends'    : [
        'base',
        'stock',
        'sale',
        'sales_team',
        'mail',
        'account',
        'account_accountant',
        'purchase',
        'document',
],
    'data' : [
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/partner_view.xml',
        'views/product_view.xml',
        'views/is_account_invoice_line.xml',
        'report/layouts.xml',
        'report/report_invoice.xml',
        'report/sale_report_templates.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'qweb': [
    ],
}

