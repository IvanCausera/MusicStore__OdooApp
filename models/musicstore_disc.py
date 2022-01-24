from odoo import fields, models, api


class Disc(models.Model):
    _name = 'musicstore.disc'
    _description = 'Disc'
    _order = 'name'

    # String
    cod = fields.Char('Code')
    name = fields.Char(
        'Title',
        required=True
    )
    disc_type = fields.Selection(
        [('cd', 'CD'),
         ('cassette', 'Cassette'),
         ('vinyl', 'Vinyl'),
         ('digital', 'Digital'),
         ('other', 'Other')],
        'Type'
    )

    # Date and Time
    date_published = fields.Date('Published on')

    # Image
    image = fields.Binary('Cover')
