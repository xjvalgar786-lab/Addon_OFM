from odoo import models, fields, api


class Entrada(models.Model):
    _name = "fiesta.entrada"
    _description = "Entrada de la fiesta"

    nombre = fields.Char(string="Nombre", required=True)
    edad = fields.Integer(string="Edad", required=True)
    tipo = fields.Selection(
        [('general', 'General'), ('vip', 'VIP')],
        string="Tipo de entrada",
        required=True
    )
    precio = fields.Float(string="Precio de la entrada", required=True)
    fecha_compra = fields.Datetime(string="Fecha y hora de compra", required=True)

    # Many2many automático, apunta al mismo modelo
    actuacion_ids = fields.Many2many("fiesta.actuacion", string="Actuaciones")