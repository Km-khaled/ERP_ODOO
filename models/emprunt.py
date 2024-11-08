from odoo import models, fields

class Emprunt(models.Model):
    _name = 'tp_erp.emprunt'
    _description = 'Emprunt de Livre'

    emprunteur_id = fields.Many2one('tp_erp.emprunteur', string="Emprunteur", required=True)
    emprunt_ligne_id = fields.One2many('tp_erp.emprunt_ligne', 'emprunt_id', string="Lignes d'emprunt")
    date_debut = fields.Date(string="Date de Début", required=True)
    date_fin = fields.Date(string="Date de Fin", required=True)
    rendu = fields.Selection([('oui', 'Oui'), ('non', 'Non')], string="Rendu", default='non')

    @api.onchange('date_fin')
    def _onchange_date_fin(self):
        if self.date_fin and self.date_fin == fields.Date.today():
            self.rendu = 'oui'
        else:
            self.rendu = 'non'