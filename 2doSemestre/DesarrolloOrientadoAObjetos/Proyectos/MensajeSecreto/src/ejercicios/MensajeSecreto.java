package ejercicios;

public class MensajeSecreto {
    public static void main(String[] args) {
//        // definir mensaje original
//        String mensaje = "   Hola_mundo secreto__   ";
//        // mostrar mensaje en consola
//        System.out.println(mensaje);
//
//        // Calcular y guardar el mensaje original
//        int longitudOriginal = mensaje.length();
//        System.out.println("Longitud del mensaje original: " + longitudOriginal);
//
//        // Eliminar espacios
//        String trimmed = mensaje.trim(); // trim() quita los espacios anteriores
//
//        // mostrar mensaje despues de trimp
//        System.out.println("Mensaje despues del trim: " + trimmed);
//
//        // remplaza los guiones bajos por espacios
//        String reemplazo = trimmed.replace("_", " ");
//        System.out.println("Mensaje despues del remplazo: " + reemplazo);
//
//        // colapsar dobles espacios (si aparecen) y hacer trim final
//        reemplazo = reemplazo.replace("  ", " "); // convierte "  " → " "
//        String procesado = reemplazo.trim();       // quitar posibles espacios al inicio o final
//
//// Mostrar mensaje procesado final
//        System.out.println("Mensaje procesado: " + procesado);
//        System.out.println("Longitud del mensaje procesado: " + procesado.length());
//

    // charAt (int index) -> devuelve el caracter en la posicion indicada.

        char a = 'a';

        String mensaje = "Hola, bienvenido a la clase de POO!";
        char primeraLetra = mensaje.charAt(0);
        System.out.println("charAt(0): " + primeraLetra);

    // indexOf (String s) -> devuelve la posición de la primera ocurrencia.
        System.out.println("indexOf('Hola'): " + mensaje.indexOf("Hola"));
        System.out.println("indexOf('la'): " + mensaje.indexOf("la"));
        System.out.println("indexOf('chao'): " + mensaje.indexOf("chao"));
        System.out.println("toUpperCase: " + mensaje.toUpperCase());
        System.out.println("toLowerCase: " + mensaje.toLowerCase());

    //startsWith (String s) -> verifica si empieza con un texto.
        System.out.println("startWith: " + mensaje.startsWith("Hola"));
        System.out.println("startWith: " + mensaje.startsWith("hola"));


        //endsWith(String s) -> verifica si termina con un texto.
        System.out.println("endtWith: " + mensaje.endsWith("OO!"));
        System.out.println("endtWith: " + mensaje.endsWith("OO"));

        String mnsjCapitalizar = "hoLA, bieEnvENido A la CLaSe dE Poo!";
        char primeLetra = mnsjCapitalizar.charAt(0);
        String primeLetraS = (" ")
    }
}