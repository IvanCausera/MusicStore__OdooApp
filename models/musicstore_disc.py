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
    stock = fields.Integer()

    # Date and Time
    date_published = fields.Date('Published on')
    duration = fields.Float(compute='_compute_sumaTotal')

    # Image
    image = fields.Binary('Cover')

    company_id = fields.Many2one(
        'musicstore.recordcompany',
        string='Company Records'
    )

    group_id = fields.Many2many(
        'musicstore.group',
        string='Groups'
    )

    song_ids = fields.Many2many(
        'musicstore.song',
        string='Songs'
    )

    @api.depends('song_ids')
    def _compute_sumaTotal(self):
        for disc in self:
            disc.duration = 0
            for song in disc.song_ids:
                disc.duration += song.time
