def move_motor_forward_timed(motor, time, speed) -> None:
    """Move motor forward by specified time and speed. Positive speed moves backward."""
    motor.run_timed(time_sp=time, speed_sp=speed)


def move_motor_forever(motor, speed) -> None:
    """Moves motor forever. Positive speed moves backward."""
    motor.run_forever(speed_sp=speed)


def stop_motor(motor, action: str) -> None:
    """Stops motor with the specified action"""
    motor.stop(stop_action=action)
