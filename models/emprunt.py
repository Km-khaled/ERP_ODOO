# models/emprunt.py
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Emprunt(models.Model):
    _name = 'tp_erp.emprunt'
    _description = 'Emprunt de Livre'

    emprunteur_id = fields.Many2one('tp_erp.emprunteur', string="Emprunteur", required=True, ondelete='cascade')
    emprunt_ligne_id = fields.One2many('tp_erp.emprunt_ligne', 'emprunt_id', string="Lignes d'emprunt", ondelete='cascade')
    date_debut = fields.Date(string="Date de Début", default=fields.Date.today, readonly=True, required=True)
    date_fin = fields.Date(string="Date de Fin", required=True)
    rendu = fields.Selection([('oui', 'Oui'), ('non', 'Non')], string="Rendu", default='non')

    @api.onchange('date_fin')
    def _onchange_date_fin(self):
        if self.date_fin and self.date_fin == fields.Date.today():
            self.rendu = 'oui'
        else:
            self.rendu = 'non'

    @api.constrains('date_fin')
    def _check_date_fin(self):
        for record in self:
            if record.date_fin < record.date_debut:
                raise ValidationError("La date de fin ne peut pas être antérieure à la date de début.")