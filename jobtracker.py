
import json
from datetime import date

applications = [
    {"company": "Google", "role": "Python Developer", "status": "Interview", "date": "2026-10-20"},
    {"company": "Infosys", "role": "Web Developer", "status": "Applied", "date": "2026-10-22"},
    {"company": "TCS", "role": "Software Engineer", "status": "Rejected", "date": "2026-10-23"}
]

def add_application(company, role):
    applications.append({
        "company": company,
        "role": role,
        "status": "Applied",
        "date": str(date.today())
    })

def search_application(value):
    for app in applications:
        if app["company"].lower() == value.lower() or app["status"].lower() == value.lower():
            print(app)

def update_status(company, status):
    for app in applications:
        if app["company"].lower() == company.lower():
            app["status"] = status
            print("Status updated!")
            return
    print("Application not found.")

def summary():
    print("\nApplication Summary")
    for status in ["Applied", "Interview", "Selected", "Rejected"]:
        count = sum(1 for app in applications if app["status"] == status)
        print(status, ":", count)

    print("\nInterview Applications:")
    for app in applications:
        if app["status"] == "Interview":
            print(app["company"], "-", app["role"])

add_application("Wipro", "Python Developer")
search_application("Interview")
update_status("Infosys", "Interview")
summary()

with open("tracker_report.txt", "w") as file:
    file.write("JOB APPLICATION TRACKER\n\n")
    file.write(json.dumps(applications, indent=4))
    file.write("\n\nAPPLICATION SUMMARY\n")

    for status in ["Applied", "Interview", "Selected", "Rejected"]:
        count = sum(1 for app in applications if app["status"] == status)
        file.write(f"{status}: {count}\n")

    file.write("\nInterview Applications:\n")
    for app in applications:
        if app["status"] == "Interview":
            file.write(f'{app["company"]} - {app["role"]}\n')

with open("applications.json", "w") as file:
    json.dump(applications, file, indent=4)

print("\nTracker saved successfully!")
