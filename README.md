# Agente Inteligente de Análisis de Ventas

Proyecto desarrollado usando Agentic AI para análisis de ventas mediante lenguaje natural, integración con SQL y generación dinámica de resultados visuales y exportables.

---

# Objetivo

Construir un agente inteligente capaz de: 

- Interpretar preguntas en lenguaje natural 
- Generar consultas SQL automáticamente
- Consultar una base de datos SQLite
- Mostrar resultados en tablas y gráficos
- Exportar resultados a archivos CSV
- Mantener historial conversacional
- Ejecutarse completamente en Docker

---

# Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| LangGraph | Orquestación del agente |
| LangChain | Integración con LLM |
| Streamlit | Interfaz web |
| SQLite | Base de datos |
| Pandas | Manipulación de datos |
| Plotly | Visualizacion de gráficas |
| Docker | Contenedorización |
| OpenRouter | Acceso al modelo LLM |

# Arquitectura del proyecto 

```text
Usuario (Web Streamlit)
        |
Agente IA (langGraph)
        |
Modelo de Lenguaje (LLM)
        |
Herramientas:

    |-- SQL Tool
    
    |-- Chart Tool

    |-- Export Tool
            |

SQLite
```
# Estructura del proyecto

agente-ventas/
│

├── app/

│   ├── database/

│   │   ├── ventas.csv

│   │   └── create_db.py

│   │

│   ├── prompts/

│   │   └── router_prompt.txt

│   │

│   ├── tools/

│   │   ├── sql_tool.py

│   │   ├── chart_tool.py

│   │   └── export_tool.py

│   │

│   ├── graph.py

│   ├── web.py

│   └── main.py

│

├── Dockerfile

├── docker-compose.yml

├── requirements.txt

├── .env.example

└── README.md

# Base de datos

Se utiliza SQLite con una tabla llamada Ventas
    
## Estructura

    Id - Integer
    vendedor - Text
    sede - Text
    producto - Text
    cantidad - Integer
    precio - Float
    fecha - Text

# Acceso Web 

```
http://localhost:8501
```

# Visualización de datos

El agente puede generar gráficos dinámicamente usando Plotly

Tipos de salida:

- Tabla
- Gráfico
- Archivo CSV
- Respuesta Textual  

# Ejemplos

Top 5 productos más vendidos en Medellín

Quién fue el vendedor con más ventas en Bogotá

Muéstrame gráficamente las ventas por vendedor

Necesito descargar el resumen de ventas
