import datetime
import time
from playsound import playsound

# Ventana emergente
from plyer import notification


sound_file_name = "files/SpaceLaserShotPE1095407.wav" # laser 1 sec
#sound_file_name = "files/CrixCicadasLoopNigPE925806.wav" # cicadas 6 sec
#sound_file_name = "files/Ak47MachineGunBursPE401604.wav" # gun 5 sec

ratio = 1

minutes_check = {
    50: "Pomd Start",
    59: "Pomd Finish"
}

routine_1 = { 
    "07:00": "RUN CHECK-LIST: Wake Up",
    "11:30": "RUN CHECK-LIST: Get ready to go out",
    "16:00": "RUN CHECK-LIST: Post work",
    "19:30": "Go out: Evolve presential",
    "22:30": "RUN CHECK-LIST: Pre-sleep, read something"
}

routine_2 = { 
    "07:00": "RUN CHECK-LIST: Wake Up",
    "11:30": "RUN CHECK-LIST: Get ready to go out",
    "16:00": "RUN CHECK-LIST: Post work",
    "19:20": "Go out: Evolve presential",
    "22:30": "RUN CHECK-LIST: Pre-sleep, read something"
}

routine_3 = { 
    "07:00": "RUN CHECK-LIST: Wake Up",
    "12:00": "Thesis, lunch",
    "14:00": "Work",
    "16:00": "Thesis meet",
    "17:30": "Snack, Take a shower, get ready to go out",
    "18:45": "Gym: Go out",
    "22:30": "RUN CHECK-LIST: Pre-sleep, read something"
}

alarms_check = {
    1: routine_1,
    2: routine_1,
    3: routine_1,
    4: routine_2,
    5: routine_3
}

# Used to don't repeat sound in specific minute
current_minutes_check = -1
current_alarms_check = ''

# Configura el título y el mensaje de la notificación
def notify(message, title="Recordatorio"):
    notification.notify(
        title=title,
        message=message,
        app_name="Reloj",
        timeout=10
    )

while True:
    try:
        current_time = datetime.datetime.now().time()
        current_minute = current_time.minute
        current_hour = current_time.hour
        current_second = current_time.second
        current_day = datetime.datetime.now().weekday()  + 1
        current_time_str = f'{str(current_hour).zfill(2)}:{str(current_minute).zfill(2)}'
        full_current_time_str = f'{str(current_hour).zfill(2)}:{str(current_minute).zfill(2)}:{str(current_second).zfill(2)}'
        sound = False
        
        # all minutes
        if current_minute in minutes_check and current_minutes_check != current_minute:
            print(f'{full_current_time_str} {minutes_check[current_minute]}')
            notify(minutes_check[current_minute])
            current_minutes_check = current_minute
            sound = True        
        
        """
        # fixed hours         
        if current_day in alarms_check and current_alarms_check != current_time_str:
            alarms = alarms_check[current_day]
            if current_time_str in alarms:
                print(f'{full_current_time_str} {alarms[current_time_str]}')
                notify(alarms[current_time_str])                
                sound = True
            current_alarms_check = f'{str(current_hour).zfill(2)}:{str(current_minute).zfill(2)}'
        """ 
        if sound:
            playsound(sound_file_name)
                
        #print(f'{str(current_hour).zfill(2)}:{str(current_minute).zfill(2)}:{str(current_second).zfill(2)}, sleeping')
        
    except Exception as e:
        print(f'Error: {e}')
    
    time.sleep(ratio)

