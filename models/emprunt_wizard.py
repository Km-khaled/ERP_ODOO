# models/emprunt_wizard.py
from odoo import models, fields, api
from datetime import timedelta

class EmpruntWizard(models.TransientModel):
    _name = 'tp_erp.emprunt_wizard'
    _description = 'Assistant pour ajouter un emprunt'

    emprunteur_id = fields.Many2one('tp_erp.emprunteur', string="Emprunteur", required=True)
    livre_ids = fields.Many2many('tp_erp.livre', string="Livres")

    @api.model
    def default_get(self, fields):
        res = super(EmpruntWizard, self).default_get(fields)
        if self._context.get('active_id'):
            res['emprunteur_id'] = self._context.get('active_id')
        return res

    def action_add_emprunt(self):
        emprunt = self.env['tp_erp.emprunt'].create({
            'emprunteur_id': self.emprunteur_id.id,
            'date_debut': fields.Date.today(),
            'date_fin': fields.Date.today() + timedelta(days=30),
            'rendu': 'non',
        })

        ligne_vals = []
        for livre in self.livre_ids:
            ligne_vals.append((0, 0, {
                'livre_id': livre.id,
            }))
        
        emprunt.write({
            'emprunt_ligne_id': ligne_vals
        })
        
        return {'type': 'ir.actions.act_window_close'}