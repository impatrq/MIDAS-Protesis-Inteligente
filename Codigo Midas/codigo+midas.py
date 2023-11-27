import array
import machine
import math
import time
import utime



accel_x_pin = machine.ADC(0)  
accel_y_pin = machine.ADC(1)
servo_pin = machine.PWM(machine.Pin(2)) 


def read_accel_x():
    return accel_x_pin.read_u16()


def read_accel_y():
    return accel_y_pin.read_u16()


def process_emg_signal(emg_samples, window_size=5):
    return sum(emg_samples[-window_size:]) / window_size


accel_sampling_frequency = 100 


servo_update_frequency = 50  


emg_samples = []


acquisition_duration = 10


start_time = utime.ticks_ms()


while utime.ticks_diff(utime.ticks_ms(), start_time) < acquisition_duration * 1000:
  
    emg_value = read_emg()
    emg_samples.append(emg_value)

    accel_x = read_accel_x()
    accel_y = read_accel_y()

    filtered_emg_value = process_emg_signal(emg_samples)


    utime.sleep_ms(1000 // accel_sampling_frequency)


servo_pin.duty(0)


emg_pin = machine.ADC(26)
reference_pin = machine.ADC(27)
ground_pin = machine.ADC(28)


sampling_frequency = 1000  


filter_window_size = 5


emg_samples = []


acquisition_duration = 10


start_time = utime.ticks_ms()


while utime.ticks_diff(utime.ticks_ms(), start_time) < acquisition_duration * 1000:
    emg_value = read_emg()
    emg_samples.append(emg_value)
    utime.sleep_us(1000000 // sampling_frequency)  

    filtered_emg_value = apply_filter(emg_samples, filter_window_size)
    
 
print(emg_samples)



def read_emg():
    return emg_pin.read_u16()


def apply_filter(signal, window_size=5):
    return sum(signal[-window_size:]) / window_size



emg_pin = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)


buffer_size = 1000
emg_buffer = array.array('H', [0] * buffer_size)


def read_emg_signal(samples):
    for i in range(samples):
        emg_buffer[i] = emg_pin.value()
    emg_data = emg_buffer[:samples]
    return emg_data

emg_pin = machine.ADC(0)  

accel_x_pin = machine.ADC(1)
accel_y_pin = machine.ADC(2)

servo_pin = machine.PWM(machine.Pin(3)) 

def read_emg():
    return emg_pin.read_u16()


def read_accel():
    accel_x = accel_x_pin.read_u16()
    accel_y = accel_y_pin.read_u16()
    return accel_x, accel_y


def process_emg_signal(emg_samples, window_size=5):
    return sum(emg_samples[-window_size:]) / window_size


emg_sampling_frequency = 500  
accel_sampling_frequency = 100 


emg_samples = []


acquisition_duration = 10


start_time = utime.ticks_ms()


while utime.ticks_diff(utime.ticks_ms(), start_time) < acquisition_duration * 1000:
   
    emg_value = read_emg()
    emg_samples.append(emg_value)

   
    accel_x, accel_y = read_accel()

   
    filtered_emg_value = process_emg_signal(emg_samples)

  
    accel_magnitude = accel_x + accel_y


    utime.sleep_ms(1000 // emg_sampling_frequency) 


servo_pin.duty(0)



i2c = machine.I2C(0, scl=machine.Pin(9), sda=machine.Pin(8), freq=100000)
i2c.writeto(0x18, bytes([0x20, 0x0F]))
i2c.writeto(0x18, bytes([0x23, 0x80]))

data = bytearray(6)
i2c.readfrom_mem_into(0x18, 0x28 | 0x80, data)
x = (data[1] << 8 | data[0]) / 16384.0
y = (data[3] << 8 | data[2]) / 16384.0
z = (data[5] << 8 | data[4]) / 16384.0


inclinacion = math.atan2(x, math.sqrt(y*y + z*z)) * 180 / math.pi
print("Inclinación: %.2f grados" % inclinacion)


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


def calcular_angulo(inclinacion):
    
    return int(90 + inclinacion * 2)


while True:
  
    inclinacion = math.atan2(x, math.sqrt(y*y + z*z)) * 180 / math.pi

   
    angulo1 = calcular_angulo(inclinacion)
    angulo2 = calcular_angulo(inclinacion)
    angulo3 = calcular_angulo(inclinacion)
    angulo4 = calcular_angulo(inclinacion)
    angulo5 = calcular_angulo(inclinacion)

    
    servo1.duty_ns(500000 + angulo1 * 1000000 // 180)
    servo2.duty_ns(500000 + angulo2 * 1000000 // 180)
    servo3.duty_ns(500000 + angulo3 * 1000000 // 180)
    servo4.duty_ns(500000 + angulo4 * 1000000 // 180)
    servo5.duty_ns(500000 + angulo5 * 1000000 // 180)

  
    time.sleep(0.5)
