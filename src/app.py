import dash
from dash import html, dcc
import geopandas as gpd
import plotly.express as px

source_shapefile = '/media/junio/DADOS/Cloud/CODE/python/projetos/projetosPessoais/map_dash/data/Farm_Poly.shp'

farm_poly_gdf = gpd.read_file(source_shapefile)
latitude= -10.099795
longitude= -52.124246

fig = px.choropleth(
    farm_poly_gdf,
    geojson=farm_poly_gdf.geometry,
    locations=farm_poly_gdf.index,
    projection='mercator',
    color='area_ha',
    basemap_visible=False,
    center={'lat': latitude, 'lon': longitude},
    hover_data=['area_ha'],
    labels={'area_ha': 'Área (ha)'},
    title='Área de Fazendas',
    color_continuous_scale='RdYlGn_r',
    )

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Mapa de Fazendas'),
    dcc.Graph(
        figure=fig,
        id='mapa',
        style={'height': '100vh'}
    )
])

app.run_server(
    debug=True,
    port=3080,
    use_reloader=True,
    dev_tools_hot_reload=True,
    threaded=True
) 