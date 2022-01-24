{
    'name': 'Music Store Application',
    'description': 'Manage music store catalogue',
    'author': 'Iván Causera, Estella Rubio, Antonio Leiva',
    'depends': ['base'],
    'application': True,
    'data': [
        'security/musicstore_security.xml',
        'security/ir.model.access.csv',
        'views/musicstore_menu.xml',
        'views/song_view.xml'
    ]
}
