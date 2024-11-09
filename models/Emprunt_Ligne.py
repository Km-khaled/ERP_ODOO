# models/emprunt_ligne.py
from odoo import models, fields

class EmpruntLigne(models.Model):
    _name = 'tp_erp.emprunt_ligne'
    _description = 'Ligne d\'emprunt'

    emprunt_id = fields.Many2one('tp_erp.emprunt', string="Emprunt", required=True, ondelete='cascade')
    livre_id = fields.Many2one('tp_erp.livre', string="Livre", required=True)
    isbn = fields.Char(related='livre_id.isbn', string='ISBN', readonly=True)
    nbre_pages = fields.Integer(related='livre_id.nbre_pages', string="Nombre de Pages", readonly=True)
    langue_livre = fields.Selection(related='livre_id.langue_livre', string="Langue du Livre", readonly=True)