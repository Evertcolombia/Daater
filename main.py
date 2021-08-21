#!/usr/bin/python3

import typer
import os

from code import ReadFile

app = typer.Typer()

@app.command()
def start():
    typer.secho("Bienvenido...", bg=typer.colors.GREEN, bold=True)
    
    typer.echo("Selecciona un archivo en el folder online:")
    onlinefile = readfile('/Dateer/online')
    
    typer.echo("Selecciona un archivo en el folder detail:")
    detailfile = readfile('/Dateer/detail')

    if onlinefile != None and detailfile != None:
        savename = typer.prompt("Ingrese el nombre de el archivo .csv a crear")
        if savename != None:
            typer.echo(f"Se usan los archivos {onlinefile} y {detailfile}")
            typer.echo("Preparando DataFrames")
            data = exec_program(onlinefile, detailfile, savename)
            typer.echo("DataFrames cargados correctamente")
            typer.echo("Iniciando Comparacion")

            data.compare_dataFrames()
            typer.echo("Creando Nuevo archivo .csv")
            if '.csv' in savename:
                data.export_df_to_csv(savename)
            else:
                data.export_df_to_csv(savename + '.csv')
            typer.echo("Programa Terminado Correctamente")
            typer.echo("puede ver el nuevo archivo en {}".format(savename))

    else:
        typer.echo("Intenta de nuevo")
        return

def readfile(path):
    dirs = get_dirs(path)
    print_dirs(dirs)
    fileid = typer.prompt("Ingresa un numero entre {} y {}".format(0, len(dirs) -1))
    
    if int(fileid) < len(dirs):
        filename = dirs[int(fileid)]
        return dirs[int(fileid)]
    else:
        typer.echo("No existe el archivo en ese indice!")
        return None

def get_dirs(path: str):
    dirs = os.listdir(path)
    dirs = [fl for fl in dirs if fl.endswith(".csv")]
    return dirs

def print_dirs(dirs):
    for i, fl in enumerate(dirs):
        print("[{}]: {}".format(i, fl))

def exec_program(on_path, dt_path, savename):
    data = ReadFile("no_licencia")
    path = '/Daater/'
    data.open_dataFrames(
        "{}online/{}".format(path, on_path),
        "{}detail/{}".format(path, dt_path)
    )
    data.get_column_index(data._df.columns, data._df2.columns)
    return data

if __name__ == '__main__':
    app()
