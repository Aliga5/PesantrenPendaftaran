#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ref_kota(models.Model):

    _name               = "ubig.ref_kota"
    _description        = "Tabel Data Ref Kab/Kota"

    name                = fields.Char( required=True, string="Nama Kab/Kota",  help="")
    keterangan          = fields.Char( string="Keterangan",  help="")

    propinsi_id         = fields.Many2one(comodel_name="ubig.ref_provinsi",  string="Propinsi",  help="")
    kecamatan_ids       = fields.One2many(comodel_name="ubig.ref_kecamatan",  inverse_name="kota_id",  string="Kecamatan",  help="")
