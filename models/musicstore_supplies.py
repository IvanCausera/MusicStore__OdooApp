from odoo import api, exceptions, fields, models


class Supplies(models.Model):
    _name = 'musicstore.supplies'
    _description = 'Supplies Request'
    _rec_name = 'user_id'

    # Numbers
    amount_disc = fields.Integer()
    amount_songs = fields.Integer()
    order_price = fields.Float(compute='_compute_orderprice', readonly=True)

    # Dates
    request_date = fields.Date(
        default=lambda s: fields.Date.today())

    # Others
    user_id = fields.Many2one(
        'res.users',
        'Salesperson',
        default=lambda s: s.env.uid)

    provider_id = fields.Many2one(
        'res.users',
        'Provider',
        default=lambda s: s.env.uid)

    disc_ids = fields.Many2one('musicstore.disc', string='Disc')
    songs_ids = fields.Many2one('musicstore.song', string='Song')

    @api.onchange('user_id')
    def onchange_member_id(self):
        today = fields.Date.today()
        if self.request_date != today:
            self.request_date = fields.Date.today()
            return {
                'warning': {
                    'title': 'Changed Request Date',
                    'message': 'Request date changed to today.',
                }
            }

    @api.depends('disc_ids', 'songs_ids', 'amount_disc', 'amount_songs')
    def _compute_orderprice(self):
        totalDiscos = 0
        totalCancion = 0
        for disc in self.disc_ids:
            totalDiscos += disc.price * self.amount_disc
        for song in self.songs_ids:
            totalCancion += song.price * self.amount_songs
        self.order_price = totalDiscos + totalCancion
