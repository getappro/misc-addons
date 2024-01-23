# -*- coding: utf-8 -*-

from odoo import fields, models

class SaleOrder(models.Model):
    """Introduce signature in pdf reports"""
    _inherit = 'sale.order'

    company_sign = fields.Boolean(string='Signature', help='Enable it, while you '
                                                        'want to apply '
                                                        'signature on your pdf '
                                                        'reports')