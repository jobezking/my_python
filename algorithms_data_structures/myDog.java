public class myDog {
    public String name;
    private int month;
    private int day;
    private int year;
    private String birthDate;
    private String speakText;

    public myDog( String name, int month, int day, int year, String speakText) {
        this.name = name;
        this.month = month;
        this.day = day;
        this.year = year;
        this.birthDate = Integer.toString(month) + "/" + Integer.toString(day) + "/" + Integer.toString(year);
        this.speakText = speakText;
    }
}

class Dog {
    public static void main(String[] args) {
        myDog spot = new myDog("spot", 11, 1, 1992, "woof");
        System.out.println(spot.name);
    }
}