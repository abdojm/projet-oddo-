from odoo import models, fields

class TpReunion(models.Model):
    _name = "tp.reunion"
    _description = "Réunion TP"

    name = fields.Char(string="Titre de la réunion", required=True)
    responsable = fields.Char(string="Responsable")
    date_reunion = fields.Date(string="Date de la réunion")
    statut = fields.Selection([
        ("brouillon", "Brouillon"),
        ("planifiee", "Planifiée"),
        ("terminee", "Terminée"),
    ], default="brouillon")
    description = fields.Text(string="Description")

