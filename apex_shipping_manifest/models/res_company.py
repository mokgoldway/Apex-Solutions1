# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    default_license_id = fields.Many2one(comodel_name='metrc.license', string="Default Canninas Licnese",
                                        domain='[("base_type", "=", "Internal")]')
