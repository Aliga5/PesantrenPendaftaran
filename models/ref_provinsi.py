#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ref_propinsi(models.Model):

    _name               = "ubig.ref_provinsi"
    _description        = "Tabel Referensi Data Propinsi"

    name                = fields.Char( required=True, string="Nama Propinsi",  help="")
    keterangan          = fields.Char( string="Keterangan",  help="")

    kota_ids            = fields.One2many(comodel_name="ubig.ref_kota",  inverse_name="propinsi_id",  string="Kota",  help="")
