from odoo import models, fields


class Livre(models.Model):
    _name = "tp_erp.livre"
    _description = "Livre"

    titre = fields.Char(string="Titre", required=True)
    langue_livre = fields.Selection(
        [("francais", "Français"), ("arabe", "Arabe"), ("anglais", "Anglais")],
        string="Langue du Livre",
    )
    isbn = fields.Char(string='ISBN', required=True)
    nbre_pages = fields.Integer(string="Nombre de Pages")
    image_libre = fields.Binary(string="Image")
    auteur_ids = fields.Many2many("tp_erp.auteur", string="Auteurs")
    emprunt_ligne_id = fields.One2many("tp_erp.emprunt_ligne", "livre_id", string="Emprunts")

    @api.onchange('titre')
    def _onchange_titre(self):
        if self.titre:
            # Example logic to update fields based on the title
            self.isbn = "Updated ISBN based on title"
            self.langue_livre = "francais"  # Example value
            self.nbre_pages = 100  # Example value