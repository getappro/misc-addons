# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing det


from odoo import fields, models, api


class PayslipParser(models.AbstractModel):
    _name = 'report.l10n_ma_hr_reports.report_resig_accept'
    _description = ("Acception de démission")

    @api.model
    def _get_report_values(self, docids, data=None):
        resignation = self.env['hr.resignation'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'hr.resignation',
            'data': data,
            'docs': resignation,
            'lang': "fr_FR",
        }

