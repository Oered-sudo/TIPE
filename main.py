from Phidget22.Phidget import *
from Phidget22.Devices.BLDCMotor import BLDCMotor

# Motor data
KT_NM_PER_A = 5.0 / 7.0      # 5 N·m at 7 A
GEAR_RATIO = 23.0

def motor_torque_from_current(current_amps):
    motor_torque = KT_NM_PER_A * current_amps
    gearbox_torque = motor_torque * GEAR_RATIO
    return motor_torque, gearbox_torque

def output_velocity_to_motor_rps(output_rpm):
    motor_rpm = output_rpm * GEAR_RATIO
    return motor_rpm / 60.0

def main():
    motor = BLDCMotor()
    motor.setChannel(0)          # change if your motor is on another channel
    motor.setIsHubPortDevice(True)

    motor.openWaitForAttachment(5000)
    motor.setEngaged(True)

    motor.setCurrentLimit(7.0)   # safety limit
    motor.setTargetCurrent(7.0)  # torque command via current

    desired_output_rpm = 50.0    # example output shaft speed
    motor.setTargetVelocity(output_velocity_to_motor_rps(desired_output_rpm))

    motor_torque, gearbox_torque = motor_torque_from_current(7.0)
    print(f"Motor torque: {motor_torque:.3f} Nm")
    print(f"Gearbox output torque: {gearbox_torque:.1f} Nm")
    print(f"Target output speed: {desired_output_rpm} RPM")

    input("Press Enter to stop...")
    motor.setTargetVelocity(0.0)
    motor.setTargetCurrent(0.0)
    motor.setEngaged(False)
    motor.close()

if __name__ == "__main__":
    main()