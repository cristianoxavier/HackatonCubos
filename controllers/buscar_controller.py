from geopy.geocoders import Nominatim
import folium


def buscar_endereco(args):
    locator = Nominatim(user_agent="myGeocoder")
    endereco = args['endereco']
    local = locator.geocode(endereco)
    m = folium.Map(location=[local.latitude, local.longitude], zoom_start=13)
    return m
