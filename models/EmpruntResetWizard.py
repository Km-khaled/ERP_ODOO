# models/emprunt_reset_wizard.py
from odoo import models, fields, api

class EmpruntResetWizard(models.TransientModel):
    _name = 'tp_erp.emprunt.reset.wizard'
    _description = 'Assistant pour réinitialiser les emprunts'

    emprunteur_id = fields.Many2one('tp_erp.emprunteur', string="Emprunteur", required=True)

    @api.model
    def default_get(self, fields):
        res = super(EmpruntResetWizard, self).default_get(fields)
        if self._context.get('active_id'):
            res['emprunteur_id'] = self._context.get('active_id')
        return res

    def action_reset_emprunts(self):
        if self.emprunteur_id:
            self.emprunteur_id.emprunt_ids.unlink()
        return {'type': 'ir.actions.act_window_close'}