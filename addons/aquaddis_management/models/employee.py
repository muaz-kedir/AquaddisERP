from odoo import models, fields


class AquaddisEmployee(models.Model):
    _name = 'aquaddis.employee'
    _description = 'AQUADDIS Employee'
    _order = 'name'

    name = fields.Char(
        string='Employee Name',
        required=True
    )

    email = fields.Char(
        string='Email'
    )

    phone = fields.Char(
        string='Phone Number'
    )

    age = fields.Integer(
        string='Age'
    )

    gender = fields.Selection(
        [
            ('male', 'Male'),
            ('female', 'Female'),
        ],
        string='Gender'
    )

    job_title = fields.Char(
        string='Job Title'
    )

    hire_date = fields.Date(
        string='Hire Date'
    )

    department_id = fields.Many2one(
        'aquaddis.department',
        string='Department',
        ondelete='restrict'
    )

    active = fields.Boolean(
        string='Active',
        default=True
    )