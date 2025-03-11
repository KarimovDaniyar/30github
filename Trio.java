import java.util.ArrayList;
import java.util.List;

import java.util.Objects;
//
//public class Trio<A,B,C> {
//    private A trioA;
//    private B trioB;
//    private C trioC;
//
//    public Trio(A a, B b , C c){
//        trioA = a;
//        trioB = b;
//        trioC = c;
//    }
//    public String toString(){
//        return trioA+ ", " + trioB+  ", " + trioC;
//    }
//    public void display() {
//        System.out.println(trioA.toString() + ", " + trioB.toString()+  ", " + trioC.toString());
//    }
//
//    public static void main(String[] args) {
//        Trio<Integer, String,Double> t = new Trio<>(10, "Ten", 10.0);
//        t.display();
//
//        Trio<Trio,Character,Exception> newT= new Trio<>(t,'T', new Exception());
//        newT.display();
//
//        Trio<Number, Boolean, Objects> alsoNewT = new Trio(3.14, true, newT);
//        alsoNewT.display();
//    }
//}


class Storage<T> {
    List<T> array = new ArrayList<>();

    void add(T item) {
        array.add(item);
    }

    void remove(T item) {
        array.remove(item);
    }

    void display() {
        for (T item : array) {
            System.out.println(item);
        }
    }

    T getItem(int index){
        return array.get(index);
    }

    int getLen(){
        return array.size();
    }

    void printItem(List<T> items){
        System.out.println(items);
    }

    @Override
    public String toString() {
        return "Storage array= " + array;
    }

    public static void main(String[] args) {
        Storage<String> storage = new Storage<>();
        storage.add("Den");
        storage.add("Ibra");
        storage.add("Idris");
        storage.display();
        storage.remove("Den");
        System.out.println(storage.getLen());
        System.out.println(storage);
        System.out.println(storage.getItem(1));
    }
}
