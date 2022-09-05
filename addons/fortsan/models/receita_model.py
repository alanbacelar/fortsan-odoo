# -*- coding: utf-8 -*-
from odoo import api, fields, models
import requests
from urllib.parse import urlencode


class fortsanReceita(models.Model):
    _name = "fortsan.receita"
    _description = "fortsan receita"

    CNPJ = fields.Char(string="CNPJ")
    nome = fields.Char(string="Nome")
    complemento = fields.Char(string="Complemento")
    CEP = fields.Char(string="CEP")
    bairro = fields.Char(string="Bairro")
    município = fields.Char(string="Município")
    logradouro = fields.Char(string="Logradouro")
    uf = fields.Char(string="UF")
    email = fields.Char(string="E-mail")
    telefone = fields.Char(string="Telefone")
    endereco = fields.Char(string="Endereço")
