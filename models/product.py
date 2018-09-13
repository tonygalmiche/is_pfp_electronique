# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _
from odoo.addons import decimal_precision as dp



class IsFamille(models.Model):
    _name='is.famille'
    _order='name'
    name = fields.Char("Famille", required=True)


class IsSousFamille1(models.Model):
    _name='is.sous.famille1'
    _order='name'
    name = fields.Char("Sous-famille 1", required=True)


class IsSousFamille2(models.Model):
    _name='is.sous.famille2'
    _order='name'
    name = fields.Char("Sous-famille 2", required=True)

class IsEmplacementStock(models.Model):
    _name='is.emplacement.stock'
    _order='name'
    name = fields.Char("Emplacement de stock", required=True)


class ProductTemplate(models.Model):
    _inherit = "product.template"


    @api.depends('is_stock_mini', 'qty_available')
    def _is_qt_cde(self):
        for obj in self:
            qt=obj.is_stock_mini-obj.qty_available
            if qt<0:
                qt=0
            obj.is_qt_cde=qt


    is_designation_groupe   = fields.Char('Désignation groupe')
    is_lien_documentation   = fields.Char('Lien documentation')
    is_stock_mini           = fields.Integer('Stock mini')
    is_famille_id           = fields.Many2one('is.famille', 'Famille')
    is_sous_famille1_id     = fields.Many2one('is.sous.famille1', 'Sous-famille 1')
    is_sous_famille2_id     = fields.Many2one('is.sous.famille2', 'Sous-famille 2')
    is_emplacement_stock_id = fields.Many2one('is.emplacement.stock', 'Emplacement de stock')
    is_qt_cde               = fields.Float('Qt à commander', compute=_is_qt_cde, store=False, digits=dp.get_precision('Product Unit of Measure'))


class ProductSupplierinfo(models.Model):
    _inherit = "product.supplierinfo"

    is_fabriquant   = fields.Char('Fabriquant')





