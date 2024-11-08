from odoo import models, fields

class Auteur(models.Model):
    _name = 'tp_erp.auteur'
    _description = 'Auteur'
    # _rec_name = 'display_name'


    auteur_id =fields.Char(string="auteur_id")
    name = fields.Char(string="Nom", required=True)
    prenom = fields.Char(string="Prénom", required=True)
    date_naissance = fields.Date(string="Date de naissance")
    nationalite = fields.Char(string="Nationalité", default='Algérienne')
    sexe = fields.Selection([('homme', 'Homme'), ('femme', 'Femme')], string="Sexe")

    livre_ids = fields.Many2many('tp_erp.livre', string="Livres écrits")