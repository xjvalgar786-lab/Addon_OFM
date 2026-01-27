from odoo import models, fields, api

class Actuacion(models.Model):
    _name = "fiesta.actuacion"
    _description = "Actuación de la fiesta"

    name = fields.Char(string="Nombre", required=True)
    fecha_inicio = fields.Datetime(string="Fecha inicio", required=True)
    fecha_fin = fields.Datetime(string="Fecha fin", required=True)
    descripcion = fields.Text(string="Descripción de la actuación")

    entrada_ids = fields.One2many(
    comodel_name="fiesta.entrada",
    inverse_name="actuacion_id",
    string="Entradas"
)
    
    cant_entradas = fields.Integer(string="Cantidad de entradas", compute="_compute_cant_entradas", store=True)
    
    @api.depends('entrada_ids')
    def _compute_cant_entradas(self):
        for record in self:
            record.cant_entradas = len(record.entrada_ids)
    
    @api.constrains('fecha_inicio', 'fecha_fin')
    def _check_fecha_inicio_fin(self):
        for record in self:
            if record.fecha_inicio > record.fecha_fin:
                raise models.ValidationError("La fecha de inicio no puede ser posterior a la fecha de fin.")