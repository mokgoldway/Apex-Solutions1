# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _


class MetrcLicense(models.Model):

    _name = 'metrc.license'
    _description = 'Metrc License'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string='License',
        store=True,
        index=True,
        compute='_compute_license_name')
    license_number = fields.Char(
        string='License Number',
        required=True,
        index=True, track_visibility='onchange')
    base_type = fields.Selection(
        selection=[('Internal', 'Internal'), ('External', 'External')],
        required=True, string='Internal Type', default='External')
    license_type = fields.Selection(selection= [
                                    ('Adult-Use', 'Adult-Use'),
                                    ('Medical', 'Medical'),
                                    ('Both', 'Both')
                                ], string='Type')
    active = fields.Boolean(string='Active', default=True)
    issue_date = fields.Date(
        string="Issue Date", required=False,
        track_visibility='onchange')
    expire_date = fields.Date(
        string="Expiration Date", required=False,
        track_visibility='onchange')
    partner_id = fields.Many2one(
        comodel_name='res.partner', string='Contact',
        required=True, index=1, track_visibility='onchange', ondelete='restrict')
    issuer_id = fields.Many2one(
        comodel_name='res.partner', string='Issued By',
        track_visibility='onchange', domain=[('license_partner', '=', True)],
        ondelete='restrict')
    notes = fields.Text(string='Notes')

    @api.depends('license_number', 'partner_id')
    def _compute_license_name(self):
        for res in self:
            res.name = " - ".join(n for n in [res.license_number, res.partner_id.name] if n)

    # @api.model
    # def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
    #     args.append(('expire_date', '>=', fields.Date.today()))
    #     return super(MetrcLicense, self)._name_search(name=name, args=args, limit=limit, name_get_uid=name_get_uid)
