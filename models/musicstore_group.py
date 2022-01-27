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
