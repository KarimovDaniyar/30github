import java.util.*;

class Student {
    int id;
    String name;
    int age;
    Set<String> courses;

    public Student(int id, String name, int age) {
        this.id = id;
        this.name = name;
        this.age = age;
        this.courses = new HashSet<>();
    }
}

class StudentManager {
    Map<Integer, Student> students = new HashMap<>();
    
    void addStudent(int id, String name, int age) {
        students.put(id, new Student(id, name, age));
    }

    void removeStudent(int id) {
        students.remove(id);
    }

    void updateStudent(int id, String name, Integer age, Set<String> courses) {
        Student student = students.get(id);
        if (student != null) {
            if (name != null) student.name = name;
            if (age != null) student.age = age;
            if (courses != null) {
                student.courses = new HashSet<>(courses);
            }
        }
    }

    void displayStudents() {
        for (int i = 1; i <= students.size(); i++) {
            if (students.containsKey(i)) {
                System.out.println(students.get(i));
            }
        }
    }

    void searchStudentById(int id) {
        if (students.containsKey(id)) {
            System.out.println(students.get(id));
        } else {
            System.out.println("Student not found");
        }
    }

    void listStudentsByCourse(String course) {
        for (Student s : students.values()) {
            if (s.courses.contains(course)) System.out.println(s);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        StudentManager manager = new StudentManager();
        manager.addStudent(1, "Alice", 20);
        manager.addStudent(2, "Bob", 22);
        manager.addStudent(3, "Charlie", 21);
        manager.updateStudent(1, null, null, new HashSet<>(Arrays.asList("Java", "Math")));
        manager.updateStudent(2, null, null, new HashSet<>(Arrays.asList("Java", "Physics")));
        manager.updateStudent(3, null, null, new HashSet<>(Arrays.asList("Math", "Physics")));
        manager.displayStudents();
        manager.searchStudentById(2);
        manager.listStudentsByCourse("Java");
        manager.removeStudent(2);
        manager.displayStudents();
    }
}
