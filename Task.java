import java.util.*;

public class Task implements Comparable<Task> {
    String taskName;
    int priority;
    int duration;

    Task(String name, int pr, int dur) {
        taskName = name;
        priority = pr;
        duration = dur;
    }

    @Override
    public int compareTo(Task other) {
        if (priority != other.priority) {
            return Integer.compare(other.priority, priority);
        }
        return Integer.compare(duration, other.duration);
    }
}

class TaskScheduler {
    ArrayList<Task> scheduledTasks = new ArrayList<>();
    ArrayList<Task> pendingTasks = new ArrayList<>();

    void addTask(Task task) {
        scheduledTasks.add(task);
        Collections.sort(scheduledTasks);
    }

    void processTask() {
        if (scheduledTasks.size() > 0) {
            Task highest = scheduledTasks.remove(0);
            System.out.println("Processing Task: " + highest.taskName);
        } else if (pendingTasks.size() > 0) {
            Task next = pendingTasks.remove(0);
            System.out.println("Processing Task: " + next.taskName);
        }
    }

    void delayTask(String taskName) {
        for (int i = 0; i < scheduledTasks.size(); i++) {
            if (scheduledTasks.get(i).taskName.equals(taskName)) {
                Task t = scheduledTasks.remove(i);
                pendingTasks.add(t);
                System.out.println("Delaying Task: " + t.taskName);
                break;
            }
        }
    }

    void displayTasks() {
        System.out.println("Scheduled Tasks:");
        for (Task t : scheduledTasks) {
            System.out.println("Priority: " + t.priority + " Task: " + t.taskName + " Duration: " + t.duration);
        }
        System.out.println("Pending Tasks:");
        for (Task t : pendingTasks) {
            System.out.println("Priority: " + t.priority + " Task: " + t.taskName + " Duration: " + t.duration);
        }
    }
}

class Main {
    public static void main(String[] args) {
        TaskScheduler scheduler = new TaskScheduler();
        scheduler.addTask(new Task("Code Review", 3, 20));
        scheduler.addTask(new Task("System Update", 5, 45));
        scheduler.addTask(new Task("Database Backup", 2, 30));
        scheduler.addTask(new Task("Deploy New Feature", 5, 50));
        scheduler.addTask(new Task("Bug Fixing", 4, 25));

        scheduler.displayTasks();
        scheduler.processTask();
        scheduler.delayTask("Code Review");
        scheduler.displayTasks();
        scheduler.delayTask("Database Backup");
        scheduler.displayTasks();
        scheduler.processTask();
        scheduler.displayTasks();
        scheduler.processTask();
        scheduler.displayTasks();
        scheduler.processTask();
        scheduler.displayTasks();
        scheduler.processTask();
        scheduler.displayTasks();
        scheduler.processTask();
        scheduler.displayTasks();
    }
}
