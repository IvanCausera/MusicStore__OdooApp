from odoo import fields, models, api


class Song(models.Model):
    _name = 'musicstore.song'
    _description = 'Song'
    _order = 'name'
    # String
    name = fields.Char(
        'Title',
        default=None,
        index=True,
        help='Song title',
        readonly=False,
        required=True,
        translate=False
    )

