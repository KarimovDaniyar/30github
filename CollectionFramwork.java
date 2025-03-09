import java.util.*;

class Student{
    int id;
    String name;
    int age;
    Set<String> course;
    public Student(int id, String name, int age){
        this.id = id;
        this.name = name;
        this.age = age;
        this.course = new HashSet<>();
    }
}
class StudentManager{

    Map<Integer, Student> students = new HashMap<>();
    void addStudent(int id, String name, int age){
        students.put(id, new Student(id, name, age));
    }

    void removeStudent(int id){
        students.remove(id);
    }

    void updateStudent(int id, String name, int age, Set<String> courses){
        Student student = students.get(id);
        student.id = id;
        student.name = name;
        student.age = age;
        student.course = new HashSet<>(courses);
    }

    void displayStudents(){
        for (int i = 0; i < students.size(); i++) {
            System.out.println(students.get(i));
        }
    }

    void searchStudentById(int id){
        System.out.println(students.get(id));
    }

    void listStudentsByCourse(String course){
        for (Student s :students.values()){
            if(s.course.contains(course)){
                System.out.println(s);
            }
        }
    }
}

public class Collection {
    public static void main(String[] args) {
        StudentManager manager = new StudentManager();
        manager.addStudent(1, "Alice", 20);
        manager.addStudent(2, "Bob", 22);
        manager.addStudent(3, "Charlie", 21);
        manager.updateStudent(1, "Den", 19, new HashSet<>(Arrays.asList("Java", "Math")));
        manager.updateStudent(2, "Ibra", 11, new HashSet<>(Arrays.asList("Java", "Physics")));
        manager.updateStudent(3, "idris", 3, new HashSet<>(Arrays.asList("Math", "Physics")));
        manager.displayStudents();
        manager.searchStudentById(2);
        manager.listStudentsByCourse("Java");
        manager.removeStudent(2);
        manager.displayStudents();
    }
}
