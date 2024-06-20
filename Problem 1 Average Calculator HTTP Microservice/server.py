from flask import Flask, jsonify
import random
from threading import Lock

app = Flask(__name__)

# Configuration
WINDOW_SIZE = 10

# State
numbers_window = []
lock = Lock()

# Mock APIs to simulate fetching numbers
def get_primes():
    return [2,3,5,7,11]

def get_fibo():
    return [55,89,144,233,377,610,987,1597,2584,4181,6765]

def get_even():
    return [8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56]

def get_random():
    return [random.randint(1, 100) for _ in range(10)]

# Endpoint mapping
ENDPOINTS = {
    'p': get_primes,
    'f': get_fibo,
    'e': get_even,
    'r': get_random
}

def update_window(new_numbers):
    global numbers_window
    with lock:
        prev_state = numbers_window[:]
        for num in new_numbers:
            if num not in numbers_window:
                if len(numbers_window) >= WINDOW_SIZE:
                    numbers_window.pop(0)
                numbers_window.append(num)
        curr_state = numbers_window[:]
        return prev_state, curr_state

def calculate_average():
    if not numbers_window:
        return 0
    return sum(numbers_window) / len(numbers_window)

@app.route('/numbers/<number_type>', methods=['GET'])
def get_numbers(number_type):
    if number_type not in ENDPOINTS:
        return jsonify({'error': 'Invalid number type'}), 400

    new_numbers = ENDPOINTS[number_type]()
    prev_state, curr_state = update_window(new_numbers)
    avg = calculate_average()

    response = {
        'windowPrevState': prev_state,
        'windowCurrState': curr_state,
        'numbers': new_numbers,
        'avg': round(avg, 2)
    }

    return jsonify(response), 200, {'Content-Type': 'application/json'}

if __name__ == '__main__':
    app.run(port=9876)
