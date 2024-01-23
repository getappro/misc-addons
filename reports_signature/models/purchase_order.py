# -*- coding: utf-8 -*-

from odoo import fields, models

class PurchaseOrder(models.Model):
    """Introduce signature in pdf reports"""
    _inherit = 'purchase.order'

    signature = fields.Boolean(string='Signature', help='Enable it, while you '
                                                        'want to apply '
                                                        'signature on your pdf '
                                                        'reports')
