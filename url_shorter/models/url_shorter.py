# -*- coding: utf-8 -*-
import string
import random
import datetime

from odoo import models, api, fields


class UrlShorter(models.Model):
    _name = 'url.shorter'
    _sql_constraints = [
        ('token_uniq', 'uniqe(token)', 'Token must be unique!')
        ]

    def _default_token(self):
        """Generates a new, non-existing, token"""
        while True:
            token = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(11))
            if self.search_count([('token', '=', token)]) == 0:
                break
        return token

    name = fields.Char()

    token = fields.Char(
        required=True,
        default=_default_token
        )

    long_url = fields.Char(
        required=True,
        string='Long URL'
        )

    short_url = fields.Char(
        compute='_compute_short_url',
        string='Short URL'
        )

    redirect_number = fields.Integer(
        readonly=True,
        default=0,
        string='Number of redirects'
        )

    active = fields.Boolean(
        default=True
        )

    expiration_date = fields.Date(
        default=lambda self: datetime.date.today() + datetime.timedelta(days=7)
    )

    @api.multi
    @api.depends('token')
    def _compute_short_url(self):
        """Creates short url based on token"""
        SysParameters = self.env['ir.config_parameter']
        base_url = SysParameters.search([('key', '=', 'web.base.url')], limit=1).value
        for record in self:
            record.short_url = '%s/s/%s' % (base_url, record.token)

    @api.onchange('token')
    def _onchange_token(self):
        if not self.token:
            self.token = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(11))

    @api.model
    def create(self, vals):
        if 'name' not in vals:
            vals['name'] = vals['token']
        return super(UrlShorter, self).create(vals)

    @api.multi
    def write(self, vals):
        super(UrlShorter, self).write(vals)
        for record in self:
            if not record.name:
                record.write({'name': record.token})
        return True
