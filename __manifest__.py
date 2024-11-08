{
    "name": "TP ERP",
    "version": "1.0",
    "category": "Bibliothèque",
    "description": "Système de gestion de bibliothèque",
    "depends": ["project"],
    "data": [
        "security/ir.model.access.csv",
        "views/auteur_view.xml",
        "views/livre_view.xml",
        "views/emprunteur_view.xml",
        "views/emprunt_view.xml",
        "views/menus_actions.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
