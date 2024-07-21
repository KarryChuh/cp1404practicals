
import csv
from datatime import datetime
from project import Project

Menu = """
L - Load projects
S - Save projects
D - Display projects
F - Filter projects by date
A - Add new project
U - Update project
Q - Quit
"""
def load_projects(filename="projects.txt"):
    """Load projects from a file."""
    projects = []
    with open(filename, "r") as file:
        file.readline()  # Skip header
        for line in file:
            parts = line.strip().split('\t')
            project = Project(*parts)
            projects.append(project)
    return projects

def save_projects(projects, filename="projects.txt"):
    """Save projects to a file."""
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")

def display_projects(projects):
    """Display incomplete and complete projects sorted by priority."""
    incomplete_projects = [project for project in projects if not project.is_complete()]
    complete_projects = [project for project in projects if project.is_complete()]

    incomplete_projects.sort()
    complete_projects.sort()

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(project)

    print("\nComplete projects:")
    for project in complete_projects:
        print(project)

def filter_projects_by_date(projects, date):
    """Filter projects by start date."""
    filtered_projects = [project for project in projects if datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date() > date]
    filtered_projects.sort(key=lambda x: datetime.datetime.strptime(x.start_date, "%d/%m/%Y"))

    for project in filtered_projects:
        print(project)

def main():
    """Run the project management program."""
    projects = load_projects()

    while True:
        print(MENU)
        choice = input(">>> ").upper()
        if choice == 'L':
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == 'S':
            filename = input("Filename: ")
            save_projects(projects, filename)
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            date_str = input("Show projects that start after date (dd/mm/yyyy): ")
            date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
            filter_projects_by_date(projects, date)
        elif choice == 'A':
            projects.append(projects)
        elif choice == 'U':
            projects.sort(projects)
        elif choice == 'Q':
            save = input("Save projects to the default file? (Y/N): ").upper()
            if save == 'Y':
                save_projects(projects)
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()