from odoo import fields, models


class artists(models.Model):
    _name = 'musicstore.artists'
    _description = 'Artists'

    id = fields.Char('Code', required=True)
    name = fields.Char('Name', required=True)
    surname = fields.Char('Surname')
    nickname = fields.Char()
    tlf = fields.Char('Phone')
    email = fields.Char('Email')

    # group_id = fields.Many2one(
    #     'musicstore.group',
    #     string='Group'
    # )
