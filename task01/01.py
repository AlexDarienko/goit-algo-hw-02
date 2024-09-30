import queue
import threading
import time
import random

# Створити чергу заявок
request_queue = queue.Queue()

request_id = 0  # Унікальний номер заявки

def generate_request():
    global request_id
    while True:
        # Імітуємо час між заявками
        time.sleep(random.uniform(1, 3))
        request_id += 1
        request = f"Заявка №{request_id}"
        print(f"Згенеровано {request}")
        request_queue.put(request)

def process_request():
    while True:
        if not request_queue.empty():
            request = request_queue.get()
            print(f"Обробляється {request}")
            # Імітуємо час обробки заявки
            time.sleep(random.uniform(1, 2))
            print(f"Завершено {request}")
        else:
            print("Черга пуста, очікуємо нові заявки.")
            time.sleep(1)

def main():
    # Запускаємо генерацію заявок у окремому потоці
    generator_thread = threading.Thread(target=generate_request)
    generator_thread.daemon = True
    generator_thread.start()
    
    # Починаємо обробку заявок
    try:
        process_request()
    except KeyboardInterrupt: #Ctrl+C
        print("Програму завершено користувачем.")

if __name__ == "__main__":
    main()
