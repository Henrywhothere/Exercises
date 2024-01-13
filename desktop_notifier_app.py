import time
from plyer import notification


def desktop_notifier(title, message):
    notification.notify(
        title=title,
        message = message,
        app_icon = None)




def main():
    print("Desktop Notifier App")

    while True:
        try:
            title = input("Enter notification title: ")
            message = input("Enter notification message: ")
            delay = int(input("Enter delay in seconds: "))
            time.sleep(delay)
            desktop_notifier(title, message)
            
        
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print("An error occurred: {}".format(e))

if __name__ == "__main__":
    main()
