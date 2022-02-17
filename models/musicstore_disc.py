from odoo import fields, models, api


class Disc(models.Model):
    _name = 'musicstore.disc'
    _description = 'Disc'
    _order = 'name'

    # String
    cod = fields.Char('Cod', required=True, readonly=True, copy=False, default='New')
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

    price = fields.Float('Disc price', (5, 2), required=True)

    company_id = fields.Many2one(
        'musicstore.recordcompany',
        string='Company Records'
    )

    group_ids = fields.Many2many(
        'musicstore.group',
        string='Groups'
    )

    song_ids = fields.Many2many(
        'musicstore.song',
        string='Songs'
    )

    # sales_id = fields.One2many(
    #     'musicstore.sales',
    #     'disc_id'
    # )

    @api.depends('song_ids')
    def _compute_sumaTotal(self):
        for disc in self:
            disc.duration = 0
            for song in disc.song_ids:
                disc.duration += song.time

    @api.model
    def create(self, value):
        if value.get('cod', 'New') == 'New':
            value['cod'] = self.env['ir.sequence'].next_by_code('musicstore.disc') or 'New'
        result = super(Disc, self).create(value)
        return result
