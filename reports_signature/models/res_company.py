# -*- coding: utf-8 -*-

from odoo import fields, models

class ResCompany(models.Model):
    """Introduce watermark in pdf reports"""
    _inherit = 'res.company'

    signature_image = fields.Image(string='Image', help='Select the image')