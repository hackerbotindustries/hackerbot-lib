import hackerbot_helper as hp       
import time
from lazy_susan import LazySusan

class HackerHacker:
    def __init__(self, robot=None):
        if robot is None:
            self.robot = hp.ProgrammedController()
        else:
            self.robot = robot
        self.robot.init_driver()
        self.robot.activate_machine_mode()
        self.robot.leave_base()
        time.sleep(1)

    def look_around(self):
        lazy_susan = LazySusan(self.robot)
        lazy_susan.look_around()
        self.robot.move(0,65)
        time.sleep(1)
        lazy_susan.look_around()
        self.robot.move(0,65)
        time.sleep(1)

    def run(self):
        self.look_around()
        time.sleep(1)

    def cleanup(self):
        """Cleanup method to properly shut down the robot and restore terminal settings"""
        print("Cleaning up...")
        try:
            # Dock the robot
            print(self.robot.dock() )
            # time.sleep(2) 
            # Destroy the robot connection
            self.robot.destroy()
            
        except Exception as e:
            print(f"\nError during cleanup: {e}")

    def __del__(self):
        """Destructor to ensure cleanup is called"""
        self.cleanup()

if __name__ == "__main__":
    try:
        hackerhacker = HackerHacker()
        hackerhacker.run()
    except Exception as e:
        print(f"\nError during run: {e}")
    finally:
        hackerhacker.cleanup()
