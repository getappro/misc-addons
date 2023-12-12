# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing det


from odoo import fields, models, api


class AttestSalaire(models.AbstractModel):
    _name = 'report.l10n_ma_hr_reports.report_attest_trav_sal'
    _description = ("Attestation de Travail/Salaire")

    @api.model
    def _get_report_values(self, docids, data=None):
        employee = self.env['hr.employee'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'hr.employee',
            'data': data,
            'docs': employee,
            'lang': "fr_FR",
        }

