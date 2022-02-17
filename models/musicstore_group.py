from odoo import fields, models, api


class Group(models.Model):
    _name = 'musicstore.group'
    _description = 'Group'
    _order = 'name'

    # String
    id = fields.Char('Id', required=True, readonly=True, copy=False, default='New')

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

    @api.model
    def create(self, value):
        if value.get('id', 'New') == 'New':
            value['id'] = self.env['ir.sequence'].next_by_code('musicstore.group') or 'New'
        result = super(Group, self).create(value)
        return result
