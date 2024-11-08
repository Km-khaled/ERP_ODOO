from odoo import models,fields
class Emprunt_Ligne(models.Model):
    _name = 'tp_erp.emprunt_ligne'
    _description = 'Ligne d\'emprunt'

    emprunt_id = fields.Many2one('tp_erp.Emprunt_Ligne', string="Emprunt", required=True)
    livre_id = fields.Many2one('tp_erp.Emprunt_Ligne', string="Livre", required=True)
    isbn = fields.Char(string='ISBN', required=True)
    nbre_pages = fields.Integer(string="Nombre de Pages")
    langue_livre = fields.Selection([('francais', 'Français'), ('arabe', 'Arabe'), ('anglais', 'Anglais')], string="Langue du Livre")
