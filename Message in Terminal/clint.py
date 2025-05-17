#library
import socket
import threading
import time
from colorama import Fore, Back, Style, init
# Initialize colorama
init()
#animate_text
def animate_text(text, color):
    """انیمیشن نمایش پیام"""
    print(color + "MICKEY MOUSE: " + Style.RESET_ALL, end='')
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(0.1)
    print()
#receive_messages
def receive_messages(sock):
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA]
    color_index = 0
    
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if not message:
                break
            animate_text(message, colors[color_index % len(colors)])
            color_index += 1
        except:
            break
#connerct to server
def start_client():
    server_ip = ("server ipv4 addres")
    port = 12345
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect((server_ip, port))
        # ASCII Art
        print(Fore.GREEN + """
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠈⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣄⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠾⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⣤⣶⣤⣉⣿⣿⡯⣀⣴⣿⡗⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⡈⠀⠀⠉⣿⣿⣶⡉⠀⠀⣀⡀⠀⠀⠀⢻⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⢸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⢉⣽⣿⠿⣿⡿⢻⣯⡍⢁⠄⠀⠀⠀⣸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠐⡀⢉⠉⠀⠠⠀⢉⣉⠀⡜⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠘⣤⣭⣟⠛⠛⣉⣁⡜⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿
⡿⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⡀⠀⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  
        """ + Style.RESET_ALL)
        print(Fore.CYAN + f"🔗 Connected to server at {server_ip}:{port}" + Style.RESET_ALL)
        print(Fore.YELLOW + "💡 Type 'exit' to disconnect\n" + Style.RESET_ALL)
        
        receive_thread = threading.Thread(target=receive_messages, args=(client,))
        receive_thread.start()
        
        while True:
            message = input(Fore.WHITE + Back.GREEN + "💬 MY: " + Style.RESET_ALL + " ")
            if message.lower() == 'exit':
                break
            client.send(message.encode('utf-8'))
    except Exception as e:
        print(Fore.RED + f"⚠️ Connection error: {e}" + Style.RESET_ALL)
    finally:
        client.close()
        print(Fore.RED + "🔌 Disconnected from server" + Style.RESET_ALL)

start_client()