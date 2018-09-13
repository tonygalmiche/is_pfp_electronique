# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class IsSecteur(models.Model):
    _name='is.secteur'
    _order='name'
    name = fields.Char("Secteur", required=True)


class IsActivite(models.Model):
    _name='is.activite'
    _order='name'
    name = fields.Char("Activité", required=True)


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_secteur_id  = fields.Many2one('is.secteur', 'Secteur')
    is_activite_id = fields.Many2one('is.activite', 'Activité')





