{
    'name': 'AQUADDIS Management',
    'version': '1.0.0',
    'category': 'Human Resources',
    'summary': 'Employee and Department Management',
    'description': """
        AQUADDIS Management
        ===================
        Manage company employees and departments.
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_views.xml',
    ],
    'installable': True,
    'application': True,
}
