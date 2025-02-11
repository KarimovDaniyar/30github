import java.util.Scanner;

public class RegisterStudent {
    public static void main(String[] args) {
    University ait = new University();
    Student s0 = new Student(1, "Kar", "Den", "CS", 1);
    ait.addStudent(s0);
    Student s1 = new Student(2, "Alm", "Ynt", "CS", 1);
    ait.addStudent(s1);
    Course c0 = new Course("Munara", "CompSci", "CS2024",3, 20);
    ait.addCourse(c0);
    Course c1 = new Course("Emil", "WebDev", "WB2024",3, 20);
    ait.addCourse(c1);
    ait.registerStudentForCourse(1,"WB2024");

    Scanner scanner = new Scanner(System.in);
    boolean cont = true;
    String message = """
            \n1. Add student
            2. Add Course
            3. Register Student => Course
            4. All Courses
            5. All students
            6. Exit""";
    while(cont){
        System.out.println(message);
        int answer = scanner.nextInt();
        scanner.nextLine();
        switch (answer){
            case 1:
                System.out.println("ID");
                int ID = scanner.nextInt();
                scanner.nextLine();
                System.out.println("Last name");
                String lastName = scanner.nextLine();
                System.out.println("First name");
                String firstName = scanner.nextLine();
                System.out.println("major");
                String major = scanner.nextLine();
                System.out.println("year");
                int year = scanner.nextInt();
                Student s = new Student(ID, lastName, firstName, major, year);
                ait.addStudent(s);
                System.out.println(lastName + " welcome");
                break;
            case 2:
                System.out.println("prof Name");
                String professorName = scanner.nextLine();
                System.out.println("course Name");
                String courseName = scanner.nextLine();
                System.out.println("courseID");
                String courseID = scanner.nextLine();
                System.out.println("credits");
                int credits = scanner.nextInt();
                System.out.println("maxStudentQuota");
                int maxStudentQuota = scanner.nextInt();
                Course c = new Course(professorName, courseName, courseID, credits, maxStudentQuota);
                ait.addCourse(c);
                break;
            case 3:
                System.out.println("Student ID");
                int StudentID = scanner.nextInt();
                scanner.nextLine();
                System.out.println("Course ID");
                String CourseID = scanner.nextLine();
                ait.registerStudentForCourse(StudentID, CourseID);
                break;
            case 4:
                ait.getCoursesList();
                break;
            case 5:
                ait.getStudentsList();
                break;
            case 6:
                cont = false;
                break;
            case 7:
                System.out.println("Student ID");
                int sID = scanner.nextInt();
                scanner.nextLine();
                ait.studentCourses(sID);
                break;
            case 8:
                System.out.println("Course ID");
                String cID = scanner.nextLine();
                ait.courseStudents(cID);
                break;
            default:
                System.out.println("idi nah, write correct symbol pl");
            }
        }
    }
}

class Student {
    private String firstName;
    private String lastName;
    int studentID;
    private String major;
    private int year;
    int maxCredit;
    Course[] coursesList;

    public Student(int ID, String lastName, String firstName, String major, int year) {
        this.studentID = ID;
        this.lastName = lastName;
        this.firstName = firstName;
        this.major = major;
        this.year = year;
        this.coursesList = new Course[10];
        this.maxCredit = 12;
    }

    public String getFirstName() {
        return firstName;
    }

    public String getLastName() {
        return lastName;
    }

}

class Course{
    String professorName;
    String CourseName;
    String courseID;
    int maxStudentQuota;
    Student[] studentList ;
    int credits;

    public Course(String professorName, String courseName, String courseID, int credits, int maxStudentQuota) {
        this.professorName = professorName;
        CourseName = courseName;
        this.courseID = courseID;
        this.credits = credits;
        this.studentList = new Student[100];
        this.maxStudentQuota = maxStudentQuota;
    }
}

class University{
    Student[] studentsList = new Student[1000];
    Course[] coursesList = new Course[20];

    public void getStudentsList() {
        for(Student i : studentsList){
            if(i!=null) {
                System.out.println(i.getFirstName());
            }
        }
    }

    public void getCoursesList() {
        for(Course i : coursesList){
            if(i!=null){
            System.out.println(i.CourseName);
            }
        }
    }

    void addStudent(Student s){
        for(int i=0; i<studentsList.length; i++){
            if(studentsList[i] == null){
                studentsList[i] = s;
                break;
            }
        }
    }

    void addCourse(Course c){
        for(int i=0; i<coursesList.length; i++) {
            if (coursesList[i] == null) {
                coursesList[i] = c;
                break;
            }
        }
    }

    void registerStudentForCourse(int StudentID, String CourseID){
        Student student = null;
        Course course = null;

        for(Student i : studentsList){
            if(i!=null){
                if(i.studentID == StudentID){
                    student = i;
                    break;
                }
            }
        }
        for(Course i : coursesList){
            if(i!=null){
                if(i.courseID.equals(CourseID)){
                    course = i;
                    break;
                }
            }
        }

        if(student==null || course == null){
            System.out.println("Ошибка: студент или курс не найден");
            return;
        }

        for (Course c: student.coursesList){
            if(c!=null && c.courseID.equals(CourseID)){
                System.out.println("Студент уже записан на этот курс!");
                return;
            }
        }

        if(student.maxCredit >= course.credits && course.maxStudentQuota > 0){
            student.maxCredit -= course.credits;
            for(int i = 0;i<course.studentList.length; i++){
                if(course.studentList[i] == null){
                    course.studentList[i] = student;
                    course.maxStudentQuota--;
                    break;
                }
            }

            for(int i=0; i<student.coursesList.length;i++){
                if(student.coursesList[i] == null){
                    student.coursesList[i] = course;
                    break;
                }
            }
            System.out.println("Студент успешно записан на курс!");
        }else{
            System.out.println("Ошибка: нехватка кредитов или мест на курсе!");
        }
    }

    void studentCourses(int studentID) {
        for (Student i : studentsList) {
            if (i != null && i.studentID == studentID) {
                System.out.print("Курсы студента: ");
                for (Course c : i.coursesList) {
                    if (c != null) {
                        System.out.print(c.CourseName + " ");
                    }
                }
                System.out.println();
                return;
            }
        }
        System.out.println("Студент не найден!");
    }

    void courseStudents(String courseID) {
        for (Course i : coursesList) {
            if (i != null && i.courseID.equals(courseID)) {
                System.out.print("Студенты курса: ");
                for (Student s : i.studentList) {
                    if (s != null) {
                        System.out.print(s.getFirstName() + " " + s.getLastName() + " ");
                    }
                }
                System.out.println();
                return;
            }
        }
        System.out.println("Курс не найден!");
    }
}
