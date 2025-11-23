//public class PruebasString {
//
//    String a = "color";
//    //inmutabilidad
//
//    String b = a = a.replace("color", "calor");
//}


public class MainString {
    public static void main(String[] args) {
        String a = "Hola Mundo!";
        String b = new String ("Hola Mundo");
        String c = "Hola Mundo!";
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
        System.out.println("== : " + (a == b));
        System.out.println("equals: " + a.equals(b));
        System.out.println("== : " + (a == c));
        System.out.println("equals: " + (a.equals(c)));
        System.out.println("length: " + a.length());
        System.out.println("trim: " + a.trim());
        System.out.println("trim-lenght" + a.trim().length());
        System.out.println("replace: " + a.replace("!", "!!"));
    }

}