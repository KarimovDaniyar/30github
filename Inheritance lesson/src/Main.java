import java.util.Arrays;

class Main{
    static Book[] myBooks = new Book[100];
    public static void main(String[] args) {

        PrintedBook pb = new PrintedBook("The Great Gatsby", "F. Scott Fitzgerald", 1925, 15,218, "Scribner");
        EBook eb = new EBook("Java Programming for Beginners", "John Smith", 2020, 3, 4.5, "PDF");

        pb.PrintBook();

        for(Book book : Main.myBooks){
            if(book!=null){
                System.out.println(book.toString());
            }
        }
    }
}