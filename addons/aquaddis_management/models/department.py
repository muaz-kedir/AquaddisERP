from odoo import models, fields


class AquaddisDepartment(models.Model):
    _name = 'aquaddis.department'
    _description = 'AQUADDIS Department'
    _order = 'name'

    name = fields.Char(
        string='Department Name',
        required=True
    )

    description = fields.Text(
        string='Department Description'
    )

    employee_ids = fields.One2many(
        'aquaddis.employee',
        'department_id',
        string='Employees'
    )

    active = fields.Boolean(
        string='Active',
        default=True
    )