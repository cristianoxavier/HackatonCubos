from geopy.geocoders import Nominatim
from configurations.database import Conexao
import folium

db = Conexao()


def buscar_endereco(args):
    locator = Nominatim(user_agent="myGeocoder")
    endereco = args['localizacao']
    if endereco.upper() == 'BRAZIL' or endereco.upper() == 'BRASIL':
        zoom = 5
    else:
        zoom = 10
    local = locator.geocode(endereco)
    map = folium.Map(location=[local.latitude, local.longitude], zoom_start=zoom)
    query = "select * from tb_locais"

    localizacoes = db.consultar(query)

    for local in localizacoes:
        html = f'''
        <div class="pop-up-mapa-txt" style="text-align:center; font-size: 15px;">
            <span><strong>{local[1]}</strong></span><br>
            E-mail: <a href="mailto:{local[5]}">{local[5]}</a><br>
            Telefone: {local[6]}
            Endereço: {local[7]}
        </div>'''

        iframe = folium.IFrame(html,
                               width=220,
                               height=100)
        popup = folium.Popup(iframe,
                             max_width=200)
        folium.Marker([local[2],local[3]],icon=folium.Icon(icon='hand-down'), popup=popup).add_to(map)

    return map
