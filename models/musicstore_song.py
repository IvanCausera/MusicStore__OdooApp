from odoo import fields, models, api


class Song(models.Model):
    _name = 'musicstore.song'
    _description = 'Song'
    _order = 'name'
    # String
    id = fields.Char('Id', required=True, readonly=True, copy=False, default='New')

    name = fields.Char(
        'Title',
        required=True
    )

    time = fields.Float('Time', (3, 2))
    image = fields.Binary('Cover')
    price = fields.Float('Song price', (3, 2))
    stock = fields.Integer()

    # disc_ids = fields.Many2many(
    #     'musicstore.disc',
    #     string="Discs"
    # )

    @api.model
    def create(self, value):
        if value.get('id', 'New') == 'New':
            value['id'] = self.env['ir.sequence'].next_by_code('musicstore.song') or 'New'
        result = super(Song, self).create(value)
        return result
