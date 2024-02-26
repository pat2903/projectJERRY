def reset_steering(steering_motor) -> None:
    """Makes steering motor face forward"""
    steering_motor.run_to_abs_pos(position_sp=0, speed_sp=100)


def turn_steering(steering_motor, angle: int, speed:int) -> None:
    """Turn steering motor by specified angle and specified speed. Positive angle turns left."""
    steering_motor.run_to_rel_pos(position_sp=angle, speed_sp=speed)
    # why are we not using abs_pos here?

def get_current_steering_motor_pos(steering_motor) -> int:
    return steering_motor.position