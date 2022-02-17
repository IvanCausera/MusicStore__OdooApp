from odoo import fields, models, api


class recordCompany(models.Model):
    _name = 'musicstore.recordcompany'
    _description = 'Record Company'
    id = fields.Char('Id', required=True, readonly=True, copy=False, default='New')
    name = fields.Char(
        'Name',
        required=True
    )
    address = fields.Char()
    tlf = fields.Char('Phone')

    # discs_id = fields.One2many(
    #     'musicstore.disc',
    #     'company_id',
    #     string='Discs'
    # )

    discs_id = fields.Many2one(
        'musicstore.disc',
        string='Discs'
    )

    @api.model
    def create(self, value):
        if value.get('id', 'New') == 'New':
            value['id'] = self.env['ir.sequence'].next_by_code('musicstore.recordcompany') or 'New'
        result = super(recordCompany, self).create(value)
        return result
