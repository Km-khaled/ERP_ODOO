from odoo import models, fields, api

class Emprunteur(models.Model):
    _name = "tp_erp.emprunteur"
    _description = "Emprunteur"

    name = fields.Char(string="Nom", required=True)
    prenom = fields.Char(string="Prénom", required=True)
    date_naissance = fields.Date(string="Date de naissance")
    state = fields.Char(string="État")
    sexe = fields.Selection([("homme", "Homme"), ("femme", "Femme")], string="Sexe")
    nbr_emprunt = fields.Integer(string="Nombre d'emprunts", compute="_compute_nbr_emprunt")
    emprunt_ids = fields.One2many("tp_erp.emprunt", "emprunteur_id", string="Emprunts", ondelete='cascade')

    @api.depends("emprunt_ids")
    def _compute_nbr_emprunt(self):
        for record in self:
            record.nbr_emprunt = len(record.emprunt_ids)

    @api.multi
    def unlink(self):
        for record in self:
            # Delete related emprunts first
            emprunts = self.env['tp_erp.emprunt'].search([('emprunteur_id', '=', record.id)])
            for emprunt in emprunts:
                # Delete emprunt_ligne records
                emprunt.emprunt_ligne_id.unlink()
            emprunts.unlink()
        return super(Emprunteur, self).unlink()