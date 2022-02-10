from odoo import fields, models


class Group(models.Model):
    _name = 'musicstore.group'
    _description = 'Group'
    _order = 'name'

    # String
    cod = fields.Char('Code')

    name = fields.Char(
        'Nombre',
        required=True
    )

    # Other
    country = fields.Many2one(
        'res.country',
        string='Country'
    )

    disc_ids = fields.Many2many(
        'musicstore.disc',
        string='Playlist'
    )

    artists_id = fields.One2many(
        'musicstore.artists',
        'group_id',
        string='Artists'
    )
