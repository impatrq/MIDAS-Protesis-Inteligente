import array
import machine
import math
import time
import utime


# Configurar los pines GPIO para los acelerómetros y los servos
accel_x_pin = machine.ADC(0)  # Asegúrate de usar los pines correctos
accel_y_pin = machine.ADC(1)
servo_pin = machine.PWM(machine.Pin(2))  # Ejemplo de configuración de un servo en el pin GPIO 2

# Función para obtener lecturas del acelerómetro en el eje X
def read_accel_x():
    return accel_x_pin.read_u16()

# Función para obtener lecturas del acelerómetro en el eje Y
def read_accel_y():
    return accel_y_pin.read_u16()

# Función para procesar la señal EMG (usando un filtro de media móvil)
def process_emg_signal(emg_samples, window_size=5):
    return sum(emg_samples[-window_size:]) / window_size

# Configurar la frecuencia de muestreo de los acelerómetros
accel_sampling_frequency = 100  # 100 muestras por segundo

# Configurar la frecuencia de actualización de los servos
servo_update_frequency = 50  # 50 Hz (50 actualizaciones por segundo)

# Lista para almacenar las muestras EMG
emg_samples = []

# Configurar la duración de la adquisición (en segundos)
acquisition_duration = 10

# Tiempo inicial de la adquisición
start_time = utime.ticks_ms()

# Bucle principal de adquisición y procesamiento
while utime.ticks_diff(utime.ticks_ms(), start_time) < acquisition_duration * 1000:
    # Leer señales EMG
    emg_value = read_emg()
    emg_samples.append(emg_value)

    # Leer señales del acelerómetro
    accel_x = read_accel_x()
    accel_y = read_accel_y()

    # Aplicar filtrado a la señal EMG
    filtered_emg_value = process_emg_signal(emg_samples)

    # Realizar cálculos para controlar los servos según la intensidad de la señal EMG
    # Aquí puedes implementar tu lógica para controlar los servos según las señales EMG y los valores de los acelerómetros

    # Por ejemplo, si la señal EMG es alta, podrías mover el servo hacia una posición específica
    # y si la señal es baja, podrías mover el servo hacia otra posición.

    # Puedes utilizar el método duty() para configurar el ciclo de trabajo del PWM y controlar la posición del servo
    # Por ejemplo, si servo_pin es el objeto que representa al servo, puedes hacer lo siguiente:
    # servo_pin.duty(500)  # Configura el ciclo de trabajo para una posición específica

    utime.sleep_ms(1000 // accel_sampling_frequency)  # Esperar para mantener la frecuencia de muestreo de los acelerómetros

# Detener los servos al finalizar el bucle
servo_pin.duty(0)


# Configurar los pines GPIO para las entradas analógicas
emg_pin = machine.ADC(26)
reference_pin = machine.ADC(27)
ground_pin = machine.ADC(28)

# Configurar la frecuencia de muestreo
sampling_frequency = 1000  # 1000 muestras por segundo

# Configurar el tamaño de la ventana del filtro
filter_window_size = 5

# Lista para almacenar las muestras EMG
emg_samples = []

# Configurar la duración de la adquisición (en segundos)
acquisition_duration = 10

# Tiempo inicial de la adquisición
start_time = utime.ticks_ms()

# Bucle principal de adquisición
while utime.ticks_diff(utime.ticks_ms(), start_time) < acquisition_duration * 1000:
    emg_value = read_emg()
    emg_samples.append(emg_value)
    utime.sleep_us(1000000 // sampling_frequency)  # Esperar para mantener la frecuencia de muestreo

    # Aplicar filtrado a la lista de muestras
    filtered_emg_value = apply_filter(emg_samples, filter_window_size)
    
    # Aquí puedes agregar más procesamiento y análisis de las señales EMG, según tus necesidades específicas.

# Puedes mostrar los resultados en la consola o enviarlos a un dispositivo externo para su visualización.
print(emg_samples)


# Función para obtener lecturas de los electrodos
def read_emg():
    return emg_pin.read_u16()

# Función para aplicar un filtro de media móvil para suavizar la señal
def apply_filter(signal, window_size=5):
    return sum(signal[-window_size:]) / window_size


#Configuración de los pines de entrada de la señal EMG
emg_pin = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)

#Creación de un array para guardar los datos EMG
buffer_size = 1000
emg_buffer = array.array('H', [0] * buffer_size)

#Función para leer la señal EMG
def read_emg_signal(samples):
    for i in range(samples):
        emg_buffer[i] = emg_pin.value()
    emg_data = emg_buffer[:samples]
    return emg_data

# Configurar los pines GPIO para los electrodos EMG
emg_pin = machine.ADC(0)  # Asegúrate de usar el pin correcto

# Configurar los pines GPIO para los acelerómetros
accel_x_pin = machine.ADC(1)
accel_y_pin = machine.ADC(2)

# Configurar el pin GPIO para el servo
servo_pin = machine.PWM(machine.Pin(3))  # Ejemplo de configuración de un servo en el pin GPIO 3

# Función para obtener la lectura del electrodo EMG
def read_emg():
    return emg_pin.read_u16()

# Función para obtener las lecturas del acelerómetro en los ejes X e Y
def read_accel():
    accel_x = accel_x_pin.read_u16()
    accel_y = accel_y_pin.read_u16()
    return accel_x, accel_y

# Función para procesar la señal EMG (usando un filtro de media móvil)
def process_emg_signal(emg_samples, window_size=5):
    return sum(emg_samples[-window_size:]) / window_size

# Configurar la frecuencia de muestreo de los electrodos EMG y los acelerómetros
emg_sampling_frequency = 500  # 500 muestras por segundo
accel_sampling_frequency = 100  # 100 muestras por segundo

# Lista para almacenar las muestras EMG
emg_samples = []

# Configurar la duración de la adquisición (en segundos)
acquisition_duration = 10

# Tiempo inicial de la adquisición
start_time = utime.ticks_ms()

# Bucle principal de adquisición y procesamiento
while utime.ticks_diff(utime.ticks_ms(), start_time) < acquisition_duration * 1000:
    # Leer señales EMG
    emg_value = read_emg()
    emg_samples.append(emg_value)

    # Leer señales de los acelerómetros
    accel_x, accel_y = read_accel()

    # Aplicar filtrado a la señal EMG
    filtered_emg_value = process_emg_signal(emg_samples)

    # Calcular la magnitud de la aceleración (se puede usar la suma de los valores de los ejes X e Y)
    accel_magnitude = accel_x + accel_y

    # Realizar cálculos para controlar los servos según la intensidad de la señal EMG y la aceleración
    # Aquí puedes implementar tu lógica para controlar los servos según las señales EMG y los valores de los acelerómetros

    # Por ejemplo, si la señal EMG es alta y la aceleración es baja, podrías mover el servo hacia una posición específica
    # Si la señal EMG es baja y la aceleración es alta, podrías mover el servo hacia otra posición.

    # Puedes utilizar el método duty() para configurar el ciclo de trabajo del PWM y controlar la posición del servo
    # Por ejemplo, si servo_pin es el objeto que representa al servo, puedes hacer lo siguiente:
    # servo_pin.duty(500)  # Configura el ciclo de trabajo para una posición específica

    # Puedes utilizar las variables filtered_emg_value y accel_magnitude para definir tu lógica de control

    utime.sleep_ms(1000 // emg_sampling_frequency)  # Esperar para mantener la frecuencia de muestreo de los electrodos EMG

# Detener los servos al finalizar el bucle
servo_pin.duty(0)


# Configuración del acelerómetro
i2c = machine.I2C(0, scl=machine.Pin(9), sda=machine.Pin(8), freq=100000)
i2c.writeto(0x18, bytes([0x20, 0x0F])) # Configuración del acelerómetro
i2c.writeto(0x18, bytes([0x23, 0x80])) # Configuración del acelerómetro

# Leer los datos del acelerómetro
data = bytearray(6)
i2c.readfrom_mem_into(0x18, 0x28 | 0x80, data)
x = (data[1] << 8 | data[0]) / 16384.0
y = (data[3] << 8 | data[2]) / 16384.0
z = (data[5] << 8 | data[4]) / 16384.0

# Procesar los datos y obtener la inclinación del dispositivo
inclinacion = math.atan2(x, math.sqrt(y*y + z*z)) * 180 / math.pi
print("Inclinación: %.2f grados" % inclinacion)

# Configuración de los pines de los servos
servo1 = machine.PWM(machine.Pin(0))
servo2 = machine.PWM(machine.Pin(1))
servo3 = machine.PWM(machine.Pin(2))
servo4 = machine.PWM(machine.Pin(3))
servo5 = machine.PWM(machine.Pin(4))
servo1.freq(50)
servo2.freq(50)
servo3.freq(50)
servo4.freq(50)
servo5.freq(50)

# Función para calcular el ángulo del servo a partir de la inclinación
def calcular_angulo(inclinacion):
    # Ajustar los valores de acuerdo a los requerimientos de cada servo específico
    return int(90 + inclinacion * 2)

# Bucle infinito para controlar los servos
while True:
    # Leer los datos del acelerómetro
    # Código para leer los datos del acelerómetro

    # Procesar los datos y obtener la inclinación del dispositivo
    inclinacion = math.atan2(x, math.sqrt(y*y + z*z)) * 180 / math.pi

    # Calcular el ángulo correspondiente para cada servo
    angulo1 = calcular_angulo(inclinacion)
    angulo2 = calcular_angulo(inclinacion)
    angulo3 = calcular_angulo(inclinacion)
    angulo4 = calcular_angulo(inclinacion)
    angulo5 = calcular_angulo(inclinacion)

    # Ajustar los ángulos de los servos
    servo1.duty_ns(500000 + angulo1 * 1000000 // 180)
    servo2.duty_ns(500000 + angulo2 * 1000000 // 180)
    servo3.duty_ns(500000 + angulo3 * 1000000 // 180)
    servo4.duty_ns(500000 + angulo4 * 1000000 // 180)
    servo5.duty_ns(500000 + angulo5 * 1000000 // 180)

    # Esperar un tiempo antes de volver a medir la inclinación y ajustar los servos
    time.sleep(0.5)