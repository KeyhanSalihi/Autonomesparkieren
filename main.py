#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# --- Hardware-Einstellungen ---
left_motor  = Motor(Port.A)              # linker Fahrmotor
right_motor = Motor(Port.D)              # rechter Fahrmotor
line_sensor = ColorSensor(Port.S4)       # Farbsensor nach unten
extra_motor = Motor(Port.C)              # Kopf-Motor (rechts/links schauen)
ultra_sensor = UltrasonicSensor(Port.S1) # Ultraschallsensor vorne
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# --- Streckenfarben (kalibrieren!) ---
YELLOW = 55.0     # gemessener Reflexionswert Gelb (Hintergrund)
WHITE  = 85.5     # gemessener Reflexionswert Weiss (Rand)
threshold = (YELLOW + WHITE) / 2.0   # Schwelle am Übergang Gelb↔Weiss

# --- Folge welchem Rand? ---
FOLLOW_RIGHT_EDGE = True  # True = rechtem weissen Rand folgen (auf Gelb bleiben)
                          # False = linkem weissen Rand folgen

# --- PID-Regler ---
DRIVE_SPEED = 80
KP = 1.0
KI = 0.005
KD = 0.05
DT = 0.1  # s

integral = 0.0
last_error = 0.0

# --- kleine Hilfsfunktionen ---
def seen_red() -> bool:
    return line_sensor.color() == Color.RED

def distance_cm() -> int:
    return ultra_sensor.distance() // 10

def edge_error(reflection: float) -> float:
    """Fehlerdefinition für Rand-Folgen:
    - rechter Rand: threshold - reflection
    - linker Rand:  reflection - threshold
    """
    if FOLLOW_RIGHT_EDGE:
        return threshold - reflection
    else:
        return reflection - threshold

def step_line_follow():
    """Eine Regelschritt-Ausführung für den Linienfolger (Rand folgen)."""
    global integral, last_error
    reflection = line_sensor.reflection()
    error = edge_error(reflection)

    # Anti-Windup fürs Integral
    integral = max(min(integral + error * DT, 200), -200)
    derivative = (error - last_error) / DT
    turn_rate = KP * error + KI * integral + KD * derivative

    robot.drive(DRIVE_SPEED, turn_rate)
    last_error = error

# --- Hauptprogramm ---
while True:
    # --- Stop-/Navigationslogik bei Rot ---
    if seen_red():
        # sanft bremsen
        for speed in range(DRIVE_SPEED, -1, -10):
            robot.drive(speed, 0)
            wait(20)
        robot.stop()

        # zuerst rechts prüfen
        extra_motor.run_target(200, 90);  wait(200)
        right_dist = distance_cm()
        extra_motor.run_target(200, 0);   wait(200)

        if right_dist > 15:
            robot.straight(-50)
            robot.turn(90)
            # weiter dem gewählten Rand folgen bis wieder Rot
            while True:
                if seen_red():
                    robot.stop()
                    break
                step_line_follow()
                wait(int(DT * 1000))
            break

        # links prüfen
        extra_motor.run_target(200, -90); wait(200)
        left_dist = distance_cm()
        extra_motor.run_target(200, 0);   wait(200)

        if left_dist > 15:
            robot.straight(-50)
            robot.turn(-90)
            while True:
                if seen_red():
                    robot.stop()
                    break
                step_line_follow()
                wait(int(DT * 1000))
            break

        # beide Seiten blockiert -> stehen bleiben
        break

    # --- Normaler Fahrbetrieb: Rand folgen (auf Gelb bleiben) ---
    step_line_follow()
    wait(int(DT * 1000))
