import random
import pyautogui
import time

# Lista de palavras
palavras = ['one', 'dois', 'three', 'quatro', 'five', 'seis', 'seven', 'oito', 'nine', 'dez',
            'eleven', 'doze', 'thirteen', 'catorze', 'fifteen', 'dezesseis', 'seventeen', 'dezoito',
            'nineteen', 'vinte', 'twenty one', 'vinte dois', 'twenty three', 'vinte quatro', 'twenty five',
            'vinte seis', 'twenty seven', 'vinte oito', 'twenty nine', 'thirty', 'trinta um', 'thirty two',
            'trinte tres', 'thirty four', 'trinta cinco', 'amarelo', 'branco', 'castanho', 'dourado', 'esmeralda',
            'fucsia', 'gengibre', 'hortela', 'indigo', 'jade', 'kaki', 'lavanda', 'marrom', 'nevoa', 'oliva',
            'pessego', 'quasar', 'rosa', 'safira', 'turquesa', 'ultravioleta', 'violeta', 'wisteria', 'amarelo',
            'zinco']

time.sleep(4)
pyautogui.moveTo(600, 270, 1)
time.sleep(5)

# Itera sobre a lista de palavras
for palavra in palavras:
    pyautogui.click()
    time.sleep(1)
    pyautogui.write(palavra)  # Digita a palavra
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(random.randint(8, 13))
    pyautogui.moveTo(400, 130, 1)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
