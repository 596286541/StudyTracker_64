# main.py
study_records = []

def add_record():
    subject = input("Enter subject: ")
    duration = float(input("Enter duration (hours): "))
    date = input("Enter date (YYYY-MM-DD): ")
    record = {"subject": subject, "duration": duration, "date": date}
    study_records.append(record)
    print("Record added successfully!\n")

def view_records():
    if not study_records:
        print("No records found.\n")
        return
    for i, record in enumerate(study_records, 1):
        print(f"{i}. Subject: {record['subject']}, Duration: {record['duration']}h, Date: {record['date']}")
    print()

def generate_report():
    if not study_records:
        print("No records to generate report.\n")
        return
    total_time = sum(record['duration'] for record in study_records)
    print(f"Total study time: {total_time} hours")
    # Simple report - can be enhanced later
    print()

def main():
    while True:
        print("Study Tracker")
        print("1. Add Study Record")
        print("2. View All Records")
        print("3. Generate Report")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_record()
        elif choice == '2':
            view_records()
        elif choice == '3':
            generate_report()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
