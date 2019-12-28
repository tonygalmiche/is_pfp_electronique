# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class IsTypeEntreprise(models.Model):
    _name='is.type.entreprise'
    _order='name'
    name = fields.Char("Type d'entreprise", required=True)


class IsSecteur(models.Model):
    _name='is.secteur'
    _order='name'
    name = fields.Char("Secteur", required=True)


class IsSource(models.Model):
    _name='is.source'
    _order='name'
    name = fields.Char("Source", required=True)


class ResPartner(models.Model):
    _inherit = "res.partner"


    is_type_entreprise_id = fields.Many2one('is.type.entreprise', "Type d'entreprise")
    is_secteur_id         = fields.Many2one('is.secteur', 'Secteur')
    is_source_id          = fields.Many2one('is.source', 'Source')
    is_iban               = fields.Char('IBAN')
    is_bic                = fields.Char('BIC')
