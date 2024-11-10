from odoo import models, fields, api

class EmpruntWizard(models.TransientModel):
    _name = 'tp_erp.emprunt_wizard'
    _description = 'Assistant pour ajouter un emprunt'

    emprunteur_id = fields.Many2one('tp_erp.emprunteur', string="Emprunteur", required=True)
    livre_ids = fields.Many2many('tp_erp.livre', string="Livres")
    date_fin = fields.Date(string="Date de fin", required=True)

    def action_ajouter_emprunt(self):
        emprunt_vals = {
            'emprunteur_id': self.emprunteur_id.id,
            'date_debut': fields.Date.today(),
            'date_fin': self.date_fin,
            'rendu': 'non',
            'emprunt_ligne_id': [(0, 0, {'livre_id': livre.id}) for livre in self.livre_ids],
        }
        self.env['tp_erp.emprunt'].create(emprunt_vals)
        return {'type': 'ir.actions.act_window_close'}
