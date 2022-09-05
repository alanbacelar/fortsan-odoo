import werkzeug
from odoo import api, http, registry
import requests
from urllib.parse import urlencode
from geopy.geocoders import Nominatim
from odoo.exceptions import ValidationError
from datetime import date


class RegistersPlaceApi(http.Controller):

    @http.route('/fortsan/fortsan/', type='json', auth='public', website=True, cors='=', csrf=False)
    def receive_json(self, **post):
        if post:
            values = {
                'palavchav': post['palavchav'],
                'disBusca': post['disBusca'],
                'latitude': post['latitude'],
                'longitude': post['longitude'],
                'cidade': post['cidade'],
                'estado': post['estado']
            }

        responseJson = self.update_business_status(self._busca(post))
        self.remove_value(responseJson)
        self.filterData(responseJson)
        
        if responseJson:
            for x in responseJson:
                values = {
                    'name': x['name'],
                    'business_status': x['business_status'],
                    'rating': x['rating'],
                    'types': ', '.join(x['types']),
                    'user_ratings_total': x['user_ratings_total'],
                    'vicinity': x['vicinity'],
                }

                insert_record = http.request.env['fortsan.place'].sudo().create(
                    values)
                args = {'success': True, 'Message': 'Good Post',
                        'id': insert_record.id}
                return args
         

    @http.route('/fortsan/fortsan/googleApi/', type='http', auth='public', website=True, csrf=False)
    def register_notify(self, **post):
        
        if post:
            #raise ValidationError('teste')
            # return werkzeug.utils.redirect("/web/#action=364&model=fortsan.menu&view_type=list&cids=&menu_id=288")
            return werkzeug.utils.redirect("/web#action=163&menu_id=127")

        return http.request.render('fortsan.place_view_web', {
            'place_view_web': True
        })

    def registration(self, name, business_status, rating, types, user_ratings_total, vicinity):
        admins = http.request.env['fortsan.place']
        admins.sudo().create({
            'name': name,
            'business_status': business_status,
            'rating': rating,
            'types': ', '.join(types),
            'user_ratings_total': user_ratings_total,
            'vicinity': vicinity,
        })

    def filterData(self, value):
        for x in value:
            self.registration(
                x["name"],
                x["business_status"],
                x["rating"],
                x["types"],
                x["user_ratings_total"],
                x["vicinity"],
            )

    # Atualizar os nome da lista de tipes
    def update_types(self, list_value):
        update_value = []
        for x in list_value:
            if x == "drugstore":
                update_value.append('Drogaria')
            if x == "pharmacy":
                update_value.append('Farmácia')
            if x == "health":
                update_value.append('Saúde')
            if x == "point_of_interest":
                update_value.append('Ponto de interesse')
            if x == "store":
                update_value.append('Loja')
            if x == "establishment":
                update_value.append('Estabelecimento')
        return update_value

    # Atualizar os nome da lista de business_status
    def update_business_status(self, responseJson):
        update_value = []
        for x in responseJson['results']:
            if x['business_status'] == 'OPERATIONAL':
                x['business_status'] = 'Operacional'
            elif x['business_status'] == 'CLOSED_TEMPORARILY':
                x['business_status'] = 'Fechado temporariamente'
            elif x['business_status'] == 'CLOSED_PERMANENTLY':
                x['business_status'] = 'fechado permanentemente'
            x['types'] = self.update_types(x['types'])
            values = {
                'name': x['name'],
                'business_status': x['business_status'],
                'rating': x['rating'],
                'types': x['types'],
                'user_ratings_total': x['user_ratings_total'],
                'vicinity': x['vicinity'],
            }
            update_value.append(values)
        return update_value

    # remover da lista valores outlines
    def remove_value(self, value):
        for x in value:
            if ('Saúde' or 'Farmácia' or 'Drogaria') in x['types']:
                continue
            else:
                value.remove(x)

    @staticmethod
    def _busca(post):
        lat = ''
        lng = ''

        api_key = "AIzaSyDJLfZFz4st-oV8uR8wKlKV3i9H1cR7PiE"
        if post['latitude'] == '' and post['longitude'] == '':
            geolocator = Nominatim(user_agent="test_app")
            location = geolocator.geocode(
                post['cidade'] + ", " + post['estado'])
            lat = location.latitude
            lng = location.longitude

        else:
            lat = post['latitude']
            lng = post['longitude']

        places_endpoint_2 = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        params_2 = {
            "key": api_key,
            "location": f"{lat},{lng}",
            "radius": post['disBusca'],
            "keyword": post['palavchav']
        }
        params_2_encoded = urlencode(params_2)
        places_url = f"{places_endpoint_2}?{params_2_encoded}"
        r2 = requests.get(places_url)
        data = r2.json()
        
        if data['error_message'] :
             raise ValidationError(data['error_message'])
       
        return data


class RegistersReceitaApi(http.Controller):

    @http.route('/fortsan/receita/', type='json', auth='public', website=True, cors='=', csrf=False)
    def receive_json(self, **post):
        if post:
            values = {
                'cnpj': post['cnpj'],
            }
            print(values)

        responseJson = self._busca(post)
        self.registration(responseJson)

    @http.route('/fortsan/receita/receitaApi/', type='http', auth='public', website=True, csrf=False)
    def register_notify(self, **post):
        if post:
            # return werkzeug.utils.redirect("/web/#action=364&model=fortsan.menu&view_type=list&cids=&menu_id=288")
            # return werkzeug.utils.redirect("/web#action=164&menu_id=128")
            return werkzeug.utils.redirect("/web#action=181&cids=1&menu_id=129&model=crm.lead&view_type=kanban")

        return http.request.render('fortsan.receita_view_web', {
            'receita_view_web': True
        })

    def registration(self, response):
        print("================ AQUI ================\n")
        print(http.request.env['crm.lead'])
        admins = http.request.env['crm.lead']
        admins.sudo().create({
            "name": response['nome'],
            "email_from": response['email'],
            "email_normalized": response['email'],
            "phone_sanitized": response['telefone'],
            "phone": response['telefone'],
            # "message_bounce": 0,
            # "user_id": 11,
            # "company_id": 1,
            # "active": True,
            # "type": "opportunity",
            # "priority": 0,
            # "team_id": 1,
            # "stage_id": 1,
            # "color": 0,
            # "expected_revenue": 0.0,
            # "prorated_revenue": 0.00,
            # "recurring_revenue_monthly": 0.00,
            # "recurring_revenue_monthly_prorated": 0.00,
            # "date_open": date.today(),
            # "day_open":  0,
            # "day_close":  0,
            # "date_last_stage_update": date.today(),
            # "email_state":  "correct",
            # "probability":  39.85,
            # "automated_probability":  39.85,
            # "create_uid":  11,
            # "create_date": date.today(),
            # "write_uid":  11,
            # "write_date": date.today(),
        })

    @staticmethod
    def _busca(post):
        apiResponse = requests.get(
            'https://www.receitaws.com.br/v1/cnpj/'+post['cnpj'])
        data = apiResponse.json()
        return data
