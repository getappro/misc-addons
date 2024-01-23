# © 2023 GetapPRO (getap.pro)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Reports Signature",
    "version": "16.0.2.1.0",
    "author": "GetapPRO",
    "category": "Purchase",
    "website": "https://www.getap.pro",
    "depends": ["purchase","sale"],
    "license": "AGPL-3",
    "images": [],
    "data": [
        'reports/purchase_order_templates.xml',
        'reports/account_invoice_templates.xml',
        'reports/sale_order_templates.xml',
        'views/res_company_views.xml',
        'views/purchase_order_views.xml',
        'views/invoice_views.xml',
        'views/sale_order.xml',
    ],
    "installable": True,
    "auto_install": False,
}