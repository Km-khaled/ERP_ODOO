from odoo import models, fields


class Emprunteur(models.Model):
    _name = "tp_erp.emprunteur"
    _description = "Emprunteur"

    name = fields.Char(string="Nom", required=True)
    prenom = fields.Char(string="Prénom", required=True)
    date_naissance = fields.Date(string="Date de naissance")
    state = fields.Char(string="État")
    sexe = fields.Selection([("homme", "Homme"), ("femme", "Femme")], string="Sexe")
    nbr_emprunt = fields.Integer(string="Nombre d'emprunts", compute="_compute_nbr_emprunt")
    emprunt_ids = fields.One2many("tp_erp.emprunt", "emprunteur_id", string="Emprunts")

    @api.depends("emprunt_ids")
    def _compute_nbr_emprunt(self):
        for record in self:
            record.nbr_emprunt = len(record.emprunt_ids)
