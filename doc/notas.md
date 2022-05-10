# Configurando Entorno

Para crear un proyecto de inicio es recomendable crear un entorno virtual para aislar las librerias de nuestro proyecto. Para esto nos posisionamos en la carpeta donde crearemos nuestro proyecto y creamos una carpeta env (este paso es opcional) , posteriormente corremos el siguiente comando en nuestra consola

```
py -m venv env
```

Una vez creado el entorno es importante activar el mismo, es decir que todas la librerias sean instaladas en el mismo.

```
cd env/scripts
activate
cd ../..
```

Para instalar las librerias en el entorno virutal se utiliza

```
pip install {Lib}
pip install {{Lib}=={version}}
```

Una libreria recomendada para cada proyecto en python el freeze la cual permite exportar todos los paquetes instalados en el entorno virutal

```
pip install freeze
```













