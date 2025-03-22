#Ray McMillin, Course ID Code, 3/21/25

def course_query():
    courses = {}  
    
    num_courses = int(input("How many courses would you like to enter? "))
    
    for _ in range(num_courses):
        course_id = input("Enter the course ID ex. (COS 2005): ").strip()
        course_name = input("Enter the course name ex. (Python Programming): ").strip()
        
        courses[course_id] = course_name
    
    subject = input("Enter the subject ex. (COS) to search for: ").strip()

    print(f"\nCourses with subject '{subject}':")
    found = False
    for course_id, course_name in courses.items():
        if course_id.startswith(subject):
            print(f"{course_id}: {course_name}")
            found = True

    if not found:
        print(f"No courses found with subject '{subject}'.")

course_query()
