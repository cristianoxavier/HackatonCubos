from geopy.geocoders import Nominatim
import folium



def buscar_endereco(args):
    locator = Nominatim(user_agent="myGeocoder")
    endereco = args['localizacao']
    local = locator.geocode(endereco)
    map = folium.Map(location=[local.latitude, local.longitude], zoom_start=15)
    folium.Marker([local.latitude, local.longitude], icon=folium.Icon(icon='cloud'), popup="Sua localização").add_to(map)
    return map
