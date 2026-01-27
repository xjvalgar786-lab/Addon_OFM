from odoo import models, fields, api


class Entrada(models.Model):
    _name = "fiesta.entrada"
    _description = "Entrada de la fiesta"
    _rec_name = "nombre" 
    

    nombre = fields.Char(string="Nombre", required=True)
    edad = fields.Integer(string="Edad", required=True, readonly=True, compute="_compute_edad")
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento", required=True)
    tipo = fields.Selection(
        [('general', 'General'), ('vip', 'VIP')],
        string="Tipo de entrada",
        required=True,
    )
    state = fields.Selection([
    ('draft', 'Borrador'),
    ('confirmada', 'Confirmada'),
    ('usada', 'Usada'),
    ('cancelada', 'Cancelada')
], string="Estado", default='draft', tracking=True)


    precio = fields.Float(string="Precio de la entrada", readonly=True , store=True, compute = "_compute_precio")
    fecha_compra = fields.Datetime(string="Fecha y hora de compra", required=True)

    actuacion_id = fields.Many2one(
    comodel_name="fiesta.actuacion",
    string="Concierto"
)
    
    @api.constrains('edad')
    def _check_edad(self):
        for record in self:
            if record.edad < 18:
                raise models.ValidationError("No se permite la entrada a menores de edad")
    
    @api.depends('tipo')
    def _compute_precio(self):
        if self.tipo == 'vip':
            self.precio = 100.0
        if self.tipo == 'general':
            self.precio = 50.0
            
    @api.depends('fecha_nacimiento')
    def _compute_edad(self):
        today = fields.Date.today()
        for record in self:
            if record.fecha_nacimiento:
                record.edad = today.year - record.fecha_nacimiento.year
            else:
                record.edad = 0
                
    def action_confirmar(self):
        for record in self:
            record.state = 'confirmada'

    def action_usar(self):
        for record in self:
            record.state = 'usada'

    def action_cancelar(self):
        for record in self:
            record.state = 'cancelada'
    def action_reset_draft(self):
        for record in self:
            record.state = 'draft'