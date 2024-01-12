import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Reemplaza 'tu_archivo.csv' con el nombre correcto de tu archivo CSV
df = pd.read_csv('swarm_api_stats_stats.csv')

# Filtrar solo las filas que te interesan
df_filtered = df[df['Name'].isin(['/crud/caracter/', '/crud/palabra/', '/crud/palabra/exist/example',
                                  '/logic/analyze-text-videos/', '/logic/analyze-text-videos/?text=hola',
                                  '/logic/analyze-text-videos/?text=hola+extended5+aceptar',
                                  '/logic/database_config', 'web'])]

# Crear el gráfico de barras con Plotly
fig = go.Figure()

# Iterar sobre las filas y agregar barras al gráfico
for i, row in df_filtered.iterrows():
    # Construir el texto que se mostrará en la tabla
    table_text = (
        f'Total Requests: {row["Request Count"]}<br>'
        f'Failures: {row["Failure Count"]}<br>'
        f'Median Response Time: {row["Median Response Time"]}<br>'
        f'Average Response Time: {row["Average Response Time"]}<br>'
        f'Min Response Time: {row["Min Response Time"]}<br>'
        f'Max Response Time: {row["Max Response Time"]}<br>'
        f'Average Content Size: {row["Average Content Size"]}<br>'
        f'Requests/s: {row["Requests/s"]}<br>'
        f'Failures/s: {row["Failures/s"]}'
    )

    # Agregar barra principal (Total de solicitudes)
    fig.add_trace(go.Bar(
        x=[row['Name']],
        y=[row['Request Count']],
        name=f'{row["Name"]} - Total Requests',
        text=table_text,  # Esto agrega el texto directamente a la barra
        hoverinfo='text',  # Esto especifica que el texto es la información que se muestra al pasar el mouse
        marker_color='blue'  # Puedes personalizar el color aquí
    ))

    # Agregar cuadro pequeño (Fallos) dentro de cada barra
    fig.add_trace(go.Bar(
        x=[row['Name']],
        y=[row['Failure Count']],
        name=f'{row["Name"]} - Failures',
        hovertext=f'Failures: {row["Failure Count"]}',
        marker_color='black'
    ))

# Personalizar el diseño del gráfico principal
fig.update_layout(
    barmode='stack',
    yaxis=dict(title='Number of Requests'),
    xaxis=dict(title='Request Type'),
    showlegend=True,
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
)

# Crear tabla con información detallada
table = go.Figure()

table.add_trace(
    go.Table(
        header=dict(values=df.columns.tolist(),
                    fill=dict(color='paleturquoise'),
                    align='left'),
        cells=dict(values=df_filtered.transpose().values.tolist(),
                   fill=dict(color='lavender'),
                   align='left'))
)

# Mostrar el gráfico de barras
fig.show()

# Mostrar la tabla
table.show()
