# -*- coding: utf-8 -*-
from odoo import api, fields, models
import requests
from urllib.parse import urlencode


class fortsanPlace(models.Model):
    _name = "fortsan.place"
    _description = "fortsan place"


    name = fields.Char(string="Nome")
    business_status = fields.Char(string="Status do negócio")
    rating = fields.Char(string="Nível de avaliação")
    types = fields.Char(string="Tipos de negócio")
    user_ratings_total = fields.Char(string="Total de avaliação")
    vicinity = fields.Char(string="Localização")
    # place_id = fields.Char(string="")
