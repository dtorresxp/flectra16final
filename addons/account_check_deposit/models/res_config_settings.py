# Copyright 2016 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# Copyright 2018 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from flectra import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    check_deposit_offsetting_account = fields.Selection(
        related='company_id.check_deposit_offsetting_account',
    )
    check_deposit_transfer_account_id = fields.Many2one(
        related='company_id.check_deposit_transfer_account_id',
    )
