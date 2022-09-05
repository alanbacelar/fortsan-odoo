# -*- coding: utf-8 -*-
from odoo import api, fields, models
import requests
from urllib.parse import urlencode


class HospitalReceita(models.Model):
    _name = "hospital.receita"
    _description = "Hospital receita"

    dados = fields.Char(compute="busca", store=True)

    name = fields.Char(string='Name', required=True)
    outros = fields.Char(string='Outros', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'other'),
    ], required=True, default='male')
    note = fields.Text(string='Description')

    api_key = "AIzaSyDJLfZFz4st-oV8uR8wKlKV3i9H1cR7PiE"

    @api.depends('name')
    def busca(self):
        lat, lng = -5.097137219376192, -38.3695578537986

        places_endpoint_2 = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        params_2 = {
            "key": self.api_key,
            "location": f"{lat},{lng}",
            "radius": 1500,
            "keyword": "food"
        }
        params_2_encoded = urlencode(params_2)
        places_url = f"{places_endpoint_2}?{params_2_encoded}"

        print(places_url)
        r2 = requests.get(places_url)
        self.dados = r2.json()

        # base_endpoint_places = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
        # params = {
        #     "key": self.api_key,
        #     "input": "Pizzaria",
        #     "inputtype": "textquery",
        #     "fields": "place_id,formatted_address,name,geometry,permanently_closed"
        # }
        # locationbias = f"point:{lat},{lng}"
        # use_cirular = True
        # if use_cirular:
        #     radius = 10000
        #     locationbias = f"circle:{radius}@{lat},{lng}"

        # params['locationbias'] = locationbias

        # params_encoded = urlencode(params)
        # places_endpoint = f"{base_endpoint_places}?{params_encoded}"
        # print(places_endpoint)

        # r = requests.get(places_endpoint)
        # print(r.json())
        # self.dados = r.json()
