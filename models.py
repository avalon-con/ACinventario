# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ExtAlmacen(models.Model):
	_inherit = 'stock.warehouse'
	
	superficie = fields.Float(string="Superficie", help="Valor de la superficie del almacén expresado en metros cuadrados.")
	altura_max = fields.Float(string="Altura Máxima", help="Valor de la altura máxima del almacén expresada en metros.")