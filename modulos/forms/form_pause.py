import modulos.forms.base_form as base_form
import modulos.variables as var
from utn_fra.pygame_widgets import (
    Button, Label
)

def init_form_pause(dict_form_data: dict) -> dict:
    """ 
    ``Parametros:`` 
        Recibe la data del formulario en formato diccionario.

    ``¿Qué hace?:``
        Crea un formulario, y se le agregan elementos como titulos y botones para
        renderizar la vista del formulario "Pause"
        Aquí el usuario puede pausar una partida en curso, y luego volver a la misma, o volver al form "Menu"
    ``¿Qué Devuelve?:`` 
        El diccionario que creó.
    """
    form = base_form.create_base_form(dict_form_data)
    
    form['title'] = Label(
        x=var.DIMENSION_PANTALLA[0] // 2, y=var.DIMENSION_PANTALLA[1] // 2 - 250,
        text=var.MAIN_TITLE, screen=form.get('screen'), 
        font_path=var.FUENTE_SAIYAN, font_size=75, color=var.COLOR_NEGRO
    )
    form['subtitle'] = Label(
        x=var.DIMENSION_PANTALLA[0] // 2, y=var.DIMENSION_PANTALLA[1] // 2 - 175,
        text='PAUSE', screen=form.get('screen'), 
        font_path=var.FUENTE_SAIYAN, font_size=50, color=var.COLOR_NEGRO
    )
    
    form['btn_back'] = Button(
        x=var.DIMENSION_PANTALLA[0] // 2, y=var.DIMENSION_PANTALLA[1] // 2 + 175,
        text="BACK TO THE MENU", screen=form.get('screen'), 
        font_path=var.FUENTE_SAIYAN, color=var.COLOR_NEGRO,
        on_click=click_change_form, on_click_param='form_main_menu'
    )
    
    form['btn_resume'] = Button(
        x=var.DIMENSION_PANTALLA[0] // 2, y=var.DIMENSION_PANTALLA[1] // 2 + 250,
        text="BACK TO THE GAME", screen=form.get('screen'), 
        font_path=var.FUENTE_SAIYAN, color=var.COLOR_NEGRO,
        on_click=click_change_form, on_click_param='form_start_level'
    )
    
    form['widgets_list'] = [
        form.get('title'), form.get('subtitle'),
        form.get('btn_back'), form.get('btn_resume')
    ]
    
    base_form.forms_dict[form.get('name')] = form
    
    return form

def click_change_form(param: str) -> None:
    """ 
    ``Parametros:`` 
        Recibe un string con el nombre del form.

    ``¿Qué hace?:`` 
        Devuelve al usuario al form "Main Menu", o al form "start level" \n
        Para que continue la partida, dependiendo el valor recibido por params.

    ``¿Qué Devuelve?:`` 
        None.
    """
    var.SOUND_CLICK.play()
    base_form.stop_music()
    base_form.play_music(base_form.forms_dict[param])
    base_form.set_active(param)

def draw(form_dict: dict) -> None:
    """ 
    ``Parametros:`` 
        Recibe la data del formulario en formato diccionario.

    ``¿Qué hace?:`` 
        Simplemente dibuja la info que recibe por parámetro, \n
        Incluida la lista de widgets.

    ``¿Qué Devuelve?:`` 
        None.
    """
    base_form.draw(form_dict)
    base_form.draw_widgets(form_dict)

def update(form_dict: dict) -> None:
    """ 
    ``Parametros:`` 
        Recibe la data del formulario en formato diccionario.

    ``¿Qué hace?:`` 
        Simplemente actualiza la info que recibe por parámetro.
        Incluida la lista de widgets.

    ``¿Qué Devuelve?:`` 
        None.
    """
    base_form.update(form_dict)
    base_form.draw_widgets(form_dict)
