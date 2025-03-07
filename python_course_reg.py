
courses = {
    "MAT1102": {"Course": "DIFFERENTIAL CALCULUS & CO-ORDINATE GEOMETRY", "Prereq": [], "Credit": 3},
    "PHY1101": {"Course": "PHYSICS 1", "Prereq": [], "Credit": 3},
    "PHY1102": {"Course": "PHYSICS 1 LAB", "Prereq": [], "Credit": 1},
    "ENG1101": {"Course": "ENGLISH READING SKILLS & PUBLIC SPEAKING", "Prereq": [], "Credit": 3},
    "CSC1101": {"Course": "INTRODUCTION TO COMPUTER STUDIES", "Prereq": [], "Credit": 1},
    "CSC1103": {"Course": "INTRODUCTION TO PROGRAMMING LAB", "Prereq": [], "Credit": 1},
    "CSC1102": {"Course": "INTRODUCTION TO PROGRAMMING", "Prereq": [], "Credit": 3},
    "CSC1204": {"Course": "DISCRETE MATHEMATICS", "Prereq": ["MAT1102", "CSC1102"], "Credit": 3},
    "MAT1205": {"Course": "INTEGRAL CALCULUS & ORDINARY DIFFERENTIAL EQUATIONS", "Prereq": ["MAT1102"], "Credit": 3},
    "CSC1205": {"Course": "OBJECT ORIENTED PROGRAMMING 1", "Prereq": ["CSC1102", "CSC1103"], "Credit": 3},
    "PHY1203": {"Course": "PHYSICS 2", "Prereq": ["PHY1101"], "Credit": 3},
    "PHY1204": {"Course": "PHYSICS 2 LAB", "Prereq": ["PHY1102"], "Credit": 1},
    "ENG1202": {"Course": "ENGLISH WRITING SKILLS & COMMUNICATIONS", "Prereq": ["ENG1101"], "Credit": 3},
    "COE2101": {"Course": "INTRODUCTION TO ELECTRICAL CIRCUITS", "Prereq": ["PHY1101"], "Credit": 3},
    "COE2102": {"Course": "INTRODUCTION TO ELECTRICAL CIRCUITS LAB", "Prereq": ["PHY1102"], "Credit": 1},
    "CHEM1101":{"Course": "CHEMISTRY", "Prereq": ["PHY1203"], "Credit": 3},
    "MAT2101": {"Course": "COMPLEX VARIABLE,LAPLACE & Z-TRANSFORMATION", "Prereq": ["MAT1205"], "Credit": 3},
    "CSC2108": {"Course": "INTRODUCTION TO DATABASE", "Prereq": ["CSC1205"], "Credit": 3},
    "EEE2104": {"Course": "ELECTRONIC DEVICES LAB", "Prereq": ["COE2102"], "Credit": 1},
    "BBA1102": {"Course": "PRINCIPLES OF ACCOUNTING", "Prereq": ["MAT1205"], "Credit": 3},
    "EEE2103": {"Course": "ELECTRONIC DEVICES", "Prereq": ["COE2101"], "Credit": 3},
    "CSC2106": {"Course": "DATA STRUCTURE", "Prereq": ["CSC1204", "CSC1205"], "Credit": 3},
    "CSC2107": {"Course": "DATA STRUCTURE LAB", "Prereq": ["CSC1204", "CSC1205"], "Credit": 1},
    "BAE2101": {"Course": "COMPUTER AIDED DESIGN & DRAFTING", "Prereq": [], "Credit": 1},
    "CSC2211": {"Course": "ALGORITHMS", "Prereq": ["CSC2106"], "Credit": 3},
    "MAT2202": {"Course": "MATRICES, VECTORS, FOURIER ANALYSIS", "Prereq": ["MAT2101"], "Credit": 3},
    "CSC2210": {"Course": "OBJECT ORIENTED PROGRAMMING 2", "Prereq": ["CSC2106", "CSC2108"], "Credit": 3},
    "CSC2209": {"Course": "OBJECT ORIENTED ANALYSIS AND DESIGN", "Prereq": ["CSC2108"], "Credit": 3},
    "BAS2101": {"Course": "BANGLADESH STUDIES", "Prereq": ["CSC1101"], "Credit": 3},
    "EEE3101": {"Course": "DIGITAL LOGIC AND CIRCUITS", "Prereq": ["EEE2103"], "Credit": 3},
    "EEE3102": {"Course": "DIGITAL LOGIC AND CIRCUITS LAB", "Prereq": ["EEE2104"], "Credit": 1},
    "MAT3103": {"Course": "COMPUTATIONAL STATISTICS AND PROBABILITY", "Prereq": ["MAT2101"], "Credit": 3},
    "CSC3113": {"Course": "THEORY OF COMPUTATION", "Prereq": ["CSC2211"], "Credit": 3},
    "ECO3150": {"Course": "PRINCIPLES OF ECONOMICS", "Prereq": ["MAT3103"], "Credit": 2},
    "ENG2103": {"Course": "BUSINESS COMMUNICATION", "Prereq": ["BAS2101"], "Credit": 3},
    "MAT3101": {"Course": "NUMERICAL METHODS FOR SCIENCE AND ENGINEERING", "Prereq": ["MAT2202"], "Credit": 3},
    "COE3103": {"Course": "DATA COMMUNICATION", "Prereq": ["EEE3101", "EEE3102"], "Credit": 3},
    "COE3104": {"Course": "MICROPROCESSOR AND EMBEDDED SYSTEMS", "Prereq": ["EEE3101", "EEE3102"], "Credit": 3},
    "CSC3112": {"Course": "SOFTWARE ENGINEERING", "Prereq": ["CSC2209"], "Credit": 3}
}

reg_courses ={}

def add_course():
  global reg_courses
  para = '''Available courses:
   a. ARTIFICIAL INTELLIGENCE AND EXPERT SYSTEM
   b. COMPUTER NETWORKS
   c. COMPUTER ORGANIZATION AND ARCHITECTURE
   d. OPERATING SYSTEM
   e. WEB TECHNOLOGIES
   f. ENGINEERING ETHICS
   g. COMPILER DESIGN
   h.COMPUTER GRAPHICS
   i. ENGINEERING MANAGEMENT
   j. RESEARCH METHODOLOGY'''

  print(para)
  option1 = (input("Select option which course you want to add(a-j)")).lower()
  print("A course is adding...")

  if option1 == 'a':
        reg_courses["CSC3217"] = {"Course": "ARTIFICIAL INTELLIGENCE AND EXPERT SYSTEM", "Prereq": ["CSC2211", "MAT3103"], "Credit": 3}
  elif option1 == 'b':
        reg_courses["COE3206"] = {"Course": "COMPUTER NETWORKS", "Prereq": ["COE3103"], "Credit": 3}
  elif option1 == 'c':
        reg_courses["COE3205"] = {"Course": "COMPUTER ORGANIZATION AND ARCHITECTURE", "Prereq": ["COE3104"], "Credit": 3}
  elif option1 == 'd':
        reg_courses["CSC3214"] = {"Course": "OPERATING SYSTEM", "Prereq": ["CSC2211", "COE3104"], "Credit": 3, "Lab": 3}
  elif option1 == 'e':
        reg_courses["CSC3215"] = {"Course": "WEB TECHNOLOGIES", "Prereq": ["CSC3112"], "Credit": 3, "Lab": 3}
  elif option1 == 'f':
        reg_courses["EEE2216"] = {"Course": "ENGINEERING ETHICS", "Prereq": ["CSC3112", "COE3104"], "Credit": 2}
  elif option1 == 'g':
        reg_courses["CSC3216"] = {"Course": "COMPILER DESIGN", "Prereq": ["CSC3113"], "Credit": 3, "Lab": 3}
  elif option1 == 'h':
        reg_courses["CSC4118"] = {"Course": "COMPUTER GRAPHICS", "Prereq": ["CSC2211", "MAT2202"], "Credit": 3, "Lab": 3}
  elif option1 == 'i':
        reg_courses["MGT3202"] = {"Course": "ENGINEERING MANAGEMENT", "Prereq": ["EEE2216"], "Credit": 3}
  elif option1 == 'j':
        reg_courses["CSC4197"] = {"Course": "RESEARCH METHODOLOGY", "Prereq": ["100 Credits"], "Credit": 3}
  elif option1 == 0:
    print("Exiting the program...")
  else:
    print("Invalid choice")
  print(reg_courses)
  menu()



def see_registered_courses():
        global courses
        print("Seeing registered courses...")
        for course_code, course_info in reg_courses.items():
          print(f" {course_info['Course']}")
        menu()



def drop_course():
        global reg_courses

        for course_code, course_info in reg_courses.items():
              print(f"Course Code: {course_code}")
              print(f"  Course Name: {course_info['Course']}")
        course_code=input("Write Course code.").upper()

        if course_code in reg_courses:
          del reg_courses[course_code]
          print(f"Course {course_code} has been dropped.")
        else:
          print("Course not found in registered courses.")
        print("Dropping a course...")
        menu()



def complete_course():
        global reg_courses
        courses.update(reg_courses)
        reg_courses.clear()
        print("Completing a course...")
        menu()



def see_completed_courses():
        for course_code, course_info in courses.items():
          print(f"  Course Name: {course_info['Course']}")
        print("Seeing completed courses...")
        menu()



def search_course():
    search_course_name = input("Write course name").upper()

    for course_code, course_info in courses.items():
      if course_info["Course"] == search_course_name:
        print(f"Course Code: {course_code}")
        print(f"  Course Name: {course_info['Course']}")
        print(f"  Prerequisites: {course_info['Prereq']}")
        print(f"  Credit: {course_info['Credit']}")
        print("Searching for a course...")
    menu()



def check_prerequisite():
 search_course_name = input("Write course name").upper()
 for course_code, course_info in courses.items():
    if course_info["Course"] == search_course_name:
        prerequisites = course_info.get("Prereq", [])
        print(f"Prerequisites for {search_course_name} ({course_code}): {', '.join(prerequisites)}")
        print("Checking prerequisites...")
 menu()



def course_details():
    global courses
    for course_code, course_info in courses.items():
      print(f"Course Code: {course_code}")
      for key, value in course_info.items():
        print(f"  {key}: {value}")
    menu()



def menu():
  print("You can do the following operations: \n1. Add Course\n2. See registered Courses\n3. Drop Course\n4. Complete Course\n5. See completed Courses\n6. Search Course\n7. Check Prerequisite\n8. See all course details\n Press 0 to exit\nChoose what you want to do:")
  option = int(input())
  if option == 1:
    add_course()
  elif option == 2:
    see_registered_courses()
  elif option == 3:
    drop_course()
  elif option == 4:
    complete_course()
  elif option == 5:
    see_completed_courses()
  elif option == 6:
    search_course()
  elif option == 7:
    check_prerequisite()
  elif option == 8:
    course_details()
  elif option == 0:
    print("Exiting the program...")
  else:
    print("Invalid choice")
    menu()

menu()