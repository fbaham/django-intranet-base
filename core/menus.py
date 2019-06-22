MENUS = {
    'MAIN_SIDEBAR': [
        {
            "name": "Gremios",
            "icon": "fa-book",
            "url": "#",
            "validators": ["menu_generator.validators.is_authenticated"],
            "submenu": [
                {
                    "name": "Cartolas de movimientos",
                    "icon": "",
                    "url": "/cartolas_gremios/",
                },
            ],
        },
    ],
    'NAVBAR': [
        {
            "name": "Inicio",
            "icon": "fa-home",
            "url": "/",
        },
    ],
}