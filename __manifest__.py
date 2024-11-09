{
    "name": "TP ERP",
    "version": "1.0",
    "category": "Bibliothèque",
    "description": "Système de gestion de bibliothèque",
    "depends": ["project"],
    "data": [
        "security/groups.xml",
        "security/ir.model.access.csv",
        "views/emprunt_reset_wizard_view.xml",  # Load wizard view first
        "views/emprunt_wizard_view.xml",
        "views/menus_actions.xml",
        "views/auteur_view.xml",
        "views/livre_view.xml",
        "views/emprunteur_view.xml",
        "views/emprunt_view.xml",
        "views/emprunt_ligne.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}