from odoo import fields, models


class recordCompany(models.Model):
    _name = 'musicstore.recordcompany'
    _description = 'Record Company'
    cod = fields.Char('Code', required=True, readonly=True, copy=False, default='New')
    name = fields.Char(
        'Name',
        required=True
    )
    address = fields.Char()
    tlf = fields.Char('Phone')

    discs_id = fields.One2many(
        'musicstore.disc',
        'company_id',
        string='Discs'
    )
