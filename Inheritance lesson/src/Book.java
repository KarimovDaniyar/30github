public class Book {
    String title;
    String author;
    int yearPublished;
    double price;

    public Book(String title, String author, int yearPublished, double price) {
        this.title = title;
        this.author = author;
        this.yearPublished = yearPublished;
        this.price = price;
    }
    void printBookDetails(){
        System.out.println("Книга " +title+" опубликована :"+ yearPublished+", "+author);
    }

    String getBookInfo(){
        return title + author + yearPublished;
    }

    @Override
    public String toString() {
        return "Book{" +
                "title='" + title + '\'' +
                ", author='" + author + '\'' +
                ", year=" + yearPublished+
                '}';
    }
}
