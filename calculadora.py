import flet as ft
from flet import Colors
from decimal import Decimal

botoes = [
    {'operador': 'AC', 'fonte': Colors.BLACK, 'fundo': Colors.BLUE_GREY_100},
    {'operador': '±', 'fonte': Colors.BLACK, 'fundo': Colors.BLUE_GREY_100},
    {'operador': '%', 'fonte': Colors.BLACK, 'fundo': Colors.BLUE_GREY_100},
    {'operador': '÷', 'fonte': Colors.BLACK, 'fundo': Colors.ORANGE},
    {'operador': '7', 'fonte': Colors.WHITE, 'fundo': Colors.WHITE24},
    {'operador': '8', 'fonte': Colors.WHITE, 'fundo': Colors.WHITE24},
    {'operador': '9', 'fonte': Colors.WHITE, 'fundo': Colors.WHITE24},
    {'operador': '*', 'fonte': Colors.WHITE, 'fundo': Colors.ORANGE},
    {'operador': '4', 'fonte': Colors.WHITE, 'fundo': Colors.WHITE24},
    {'operador': '5', 'fonte': Colors.WHITE, 'fundo': Colors.WHITE24},
    {'operador': '6', 'fonte': Colors.WHITE, 'fundo': Colors.WHITE24},
    {'operador': '-', 'fonte': Colors.WHITE, 'fundo': Colors.ORANGE},
    {'operador': '1', 'fonte': Colors.WHITE, 'fundo': Colors.WHITE24},
    {'operador': '2', 'fonte': Colors.WHITE, 'fundo': Colors.WHITE24},
    {'operador': '3', 'fonte': Colors.WHITE, 'fundo': Colors.WHITE24},
    {'operador': '+', 'fonte': Colors.WHITE, 'fundo': Colors.ORANGE},
    {'operador': '0', 'fonte': Colors.WHITE, 'fundo': Colors.WHITE24},
    {'operador': '.', 'fonte': Colors.WHITE, 'fundo': Colors.WHITE24},
    {'operador': '=', 'fonte': Colors.WHITE, 'fundo': Colors.ORANGE},
   
] 

result = ft.Text(value = '0', color = Colors.WHITE, size = 20) 


def calculate(operador, value_at):
    try:
    
     value = eval(value_at)

    
     if operador == '%':
       value/= 100
     elif operador == '±':
        value = -value
    except:

        return 'Error'
    digits = min(abs(Decimal,(value).as_tuple().exponent),5)
    return format (value, f'.{digits}f')



def select(e):
    value_at = result.value if result.value not in ['0','erro'] else ''
    value = e.control.content.value
    
    if value.isdigit() or value == '.':
        # Digitar número ou ponto
        if result.value == '0' and value != '.':
            result.value = value
        else:
            result.value = value_at + value
    
    elif value == 'AC':
        result.value = '0'
    
    elif value == '=':
        # Calcular resultado
        try:
            resultado = eval(result.value.replace('÷', '/'))
            result.value = str(resultado)
        except:
            result.value = '0'
    
    elif value == '%':
        # Calcular porcentagem
        try:
            resultado = eval(result.value.replace('÷', '/')) / 100
            result.value = str(resultado)
        except:
            result.value = '0'
    
    elif value == '±':
        # Inverter sinal
        try:
            resultado = eval(result.value.replace('÷', '/')) * -1
            result.value = str(resultado)
        except:
            result.value = '0'
    
    else:
        # Operador (+, -, *, ÷)
        if value_at and value_at[-1] in ('÷', '*', '.', '+', '-'):
            result.value = value_at[:-1] + value
        else:
            result.value = value_at + value
    
    result.update()


display = ft.Row(
     width=250,
     controls=[result],
     alignment= 'end'
  )

botao = [
    ft.Container(
        content=ft.Text(value=b['operador'], color=b['fonte']),
        width=50,
        height=50,
        bgcolor=b['fundo'],
        border_radius=100,
        alignment=ft.alignment.center,
        on_click=select
    )
    for b in botoes
]

keyboard = ft.Row(
    width=250,
    wrap=True,  
    controls=botao,
    alignment='end'
)

def main(page: ft.Page):
    page.bgcolor = '#000000'
    page.window_resizable = False
    page.window_width = 250
    page.window_height = 380
    page.title = 'Calculadora'
    page.window_always_on_top = True
    page.add(display, keyboard)


ft.app(target=main)
