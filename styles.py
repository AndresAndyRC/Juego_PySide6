Color1 = "#FFFFFF"
Color2 = "#DAF1DE"
Color3 = "#8EB69B"
Color4 = "#235347"
Color5 = "#0B2B26"

estilos_general = f'''
    QWidget {{
        background-color: {Color1}; 
    }}

    QFrame {{
        background-color: {Color2};  
        border-radius: 10px;
    }}

    QLabel {{
        color: {Color5};  /* Color del texto */
        font-size: 20px;  /* Tamaño de la fuente */
    }}

    #titulo1 {{
        font-weight: bold;  /* Texto en negrita */
        font-size: 40px;  /* Tamaño de la fuente */
        color: {Color5};  /* Color del texto */
    }}
'''

estilos_menu = estilos_general + f''' 
    
    QLineEdit {{
        background-color: {Color3};  
        border-radius: 5px;
        padding: 10px;
        color: {Color5};
    }}

    QPushButton {{
        background-color: {Color4};  /* Color del botón */
        color: {Color2};  /* Texto del botón */
        border-radius: 5px;
        padding: 8px;
    }}

    QPushButton:hover {{
        background-color: {Color2};  /* Cambio de color al pasar el cursor */
        color: {Color4};  /* Texto del botón */
    }}


'''

estilos_juego = estilos_general + f'''

    QPushButton {{
        height: 100%;
        font-size: 40px;
        font-weight: bold;
        
    }}

    QPushButton:disabled{{
        color: {Color5};
    }}
'''    