
import time
import pyautogui

#pyautogui.click -> clica com o mouse
#pyautogui.write -> escreve um texto
#pyautogui.press aperta uma tecla
#pyautogui.hotkey -> aperta um atalho
def pausa(tempo):
    time.sleep(tempo)

def abrir_programa(nome_programa):
    pyautogui.press('win')
    pausa(2)
    pyautogui.write(nome_programa)
    pausa(1)
    pyautogui.press('enter')

programa = input("Qual programa deseja abrir? ")
input(f"Pressione Enter para abrir {programa}...")

abrir_programa(programa)


"""pausa(3)
pyautogui.press('win')
pausa(2)
pyautogui.write('bloco de notas')
pausa(1)
pyautogui.press('enter')"""