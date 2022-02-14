from odoo import fields, models, api


class Song(models.Model):
    _name = 'musicstore.song'
    _description = 'Song'
    _order = 'name'
    # String
    cod = fields.Char('Code', required=True, readonly=True, copy=False, default='New')

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

    @api.model
    def create(self, value):
        if value.get('cod', 'New') == 'New':
            value['cod'] = self.env['ir.sequence'].next_by_code('musicstore.song') or 'New'
        result = super(Song, self).create(value)
        return result
