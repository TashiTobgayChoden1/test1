from queue import Queue

class Patient:
    def __init__(self, name, appointment_time):
        self.name = name
        self.appointment_time = appointment_time

def register_patient(patient_queue):
    name = input("Enter patient's name: ")
    appointment_time = input("Enter appointment time: ")
    patient = Patient(name, appointment_time)
    patient_queue.put(patient)
    print(f"{name} has been registered for appointment at {appointment_time}")

def remove_patient(patient_queue):
    if not patient_queue.empty():
        removed_patient = patient_queue.get()
        print(f"{removed_patient.name} has met the doctor and has been removed from the queue.")
    else:
        print("Queue is empty. No patients to remove.")

def display_queue(patient_queue):
    if not patient_queue.empty():
        print("Current Patient Queue:")
        index = 1
        for patient in list(patient_queue.queue):
            print(f"{index}. {patient.name} - Appointment Time: {patient.appointment_time}")
            index += 1
    else:
        print("Queue is empty.")

def main():
    patient_queue = Queue()
    while True:
        print("\n=== Patient Registration and Appointment Scheduling ===")
        print("1. Register Patient")
        print("2. Remove Patient after Meeting Doctor")
        print("3. Display Patient Queue")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")
        if choice == "1":
            register_patient(patient_queue)
        elif choice == "2":
            remove_patient(patient_queue)
        elif choice == "3":
            display_queue(patient_queue)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()