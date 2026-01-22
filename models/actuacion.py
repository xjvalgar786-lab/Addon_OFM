from odoo import models, fields, api

class Actuacion(models.Model):
    _name = "fiesta.actuacion"
    _description = "Actuación de la fiesta"

    name = fields.Char(string="Nombre", required=True)
    fecha_inicio = fields.Datetime(string="Fecha inicio", required=True)
    fecha_fin = fields.Datetime(string="Fecha fin", required=True)
    descripcion = fields.Text(string="Descripción de la actuación")

    # Many2many automático, Odoo creará la tabla intermedia
    entrada_ids = fields.Many2many("fiesta.entrada", string="Entradas")  