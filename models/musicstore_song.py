from odoo import fields, models, api


class Song(models.Model):
    _name = 'musicstore.song'
    _description = 'Song'
    _order = 'name'
    # String
    cod = fields.Char('Code')

    name = fields.Char(
        'Title',
        required=True
    )

    time = fields.Float('Time', (3, 2))
    image = fields.Binary('Cover')

    disc_ids = fields.Many2many(
        'musicstore.disc',
        string="Discs"
    )