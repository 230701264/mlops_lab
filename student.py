students = []


def add_student():
	student_id = input("Enter student ID: ").strip()

	for student in students:
		if student["id"] == student_id:
			print("A student with that ID already exists.")
			return

	name = input("Enter student name: ").strip()
	if not student_id or not name:
		print("Student ID and name cannot be empty.")
		return

	students.append({"id": student_id, "name": name})
	print("Student added.")


def display_students():
	if not students:
		print("No students have been added yet.")
		return

	print("\nStudent list:")
	for student in students:
		print(f"ID: {student['id']} | Name: {student['name']}")


def search_students():
	query = input("Enter a student ID or name to search: ").strip().lower()
	matches = [
		student
		for student in students
		if query in student["id"].lower() or query in student["name"].lower()
	]

	if matches:
		print("\nSearch results:")
		for student in matches:
			print(f"ID: {student['id']} | Name: {student['name']}")
	else:
		print("No matching students found.")


def main():
	while True:
		print("\nStudent Management")
		print("1. Add a student")
		print("2. Display students")
		print("3. Search students")
		print("4. Exit")

		choice = input("Choose an option: ").strip()

		if choice == "1":
			add_student()
		elif choice == "2":
			display_students()
		elif choice == "3":
			search_students()
		elif choice == "4":
			print("Goodbye!")
			break
		else:
			print("Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
	main()
