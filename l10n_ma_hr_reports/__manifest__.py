# -*- coding: utf-8 -*-
##############################################################################
#
#    GetapPRO SARL
#    Copyright (C) 2019-TODAY GetapPRO(<http://www.getap.pro>).
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Moroccan HR Reports',
    'summary': 'Moroccan HR Reports for odoo 16',
    'version': '16.0.3.2.0',
    'category': 'Human Resources',
    'author':'GetapPRO',
    'maintainer': 'GetapPRO',
    'website': 'http://www.getap.pro',
    'license': 'AGPL-3',
    'depends': ['hr','hr_resignation'],
    'data': [
        'reports/l10n_ma_hr_reports.xml',
        'reports/attestation_travail_template.xml',
        'reports/attestation_salaire_template.xml',
        'reports/attest_travail_salaire_template.xml',
        'reports/attestation_domiciliation_template.xml',
        'reports/resignation_accept_template.xml',
        'views/hr_contract_view.xml',
    ],
    'application': False,
    'images': ['static/description/poster_image.png'],
}