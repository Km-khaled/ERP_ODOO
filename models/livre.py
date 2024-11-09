from odoo import models, fields , api


class Livre(models.Model):
    _name = "tp_erp.livre"
    _description = "Livre"

    titre = fields.Char(string="Titre", required=True)
    langue_livre = fields.Selection(
        [("francais", "Français"), ("arabe", "Arabe"), ("anglais", "Anglais")],
        string="Langue du Livre",
    )
    isbn = fields.Char(string="ISBN", required=True)
    nbre_pages = fields.Integer(string="Nombre de Pages")
    image_libre = fields.Binary(string="Image")
    auteur_ids = fields.Many2many("tp_erp.auteur", string="Auteurs")
    emprunt_ligne_id = fields.One2many(
        "tp_erp.emprunt_ligne", "livre_id", string="Emprunts"
    )



    @api.onchange('titre','isbn','langue_livre')
    def _onchange_livre_id(self):
        if self.emprunt_ligne_id:
            self.nbre_pages = self.emprunt_ligne_id.nbre_pages
            self.isbn = self.emprunt_ligne_id.isbn
            self.langue_livre = self.emprunt_ligne_id.langue_livre

