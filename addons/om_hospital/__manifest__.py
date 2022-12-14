# -*- coding: utf-8 -*-
{
    'name': 'Hospital Management',
    'version': '1.0',
    'summary': 'Hospital Management Software',
    'sequence': -100,
    'description': """Hospital Management Software""",
    'category': 'Productivity',
    'website': 'https://www.odoomates.tech',
    'license': 'LGPL-3',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/patient.xml',
        'views/placeApi.xml',
        'views/receitaApi.xml',
    ],
    'demo': [],
    # 'qweb': ["static/src/views/action_button.xml"],
    'installable': True,
    'application': True,
    'auto_install': False,
}
