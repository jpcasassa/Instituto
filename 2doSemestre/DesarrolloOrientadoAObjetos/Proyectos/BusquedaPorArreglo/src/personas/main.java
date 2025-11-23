package personas;

public class main {
    // Atributos o variables internas
    private String nombre;
    private int edad;
    private String correo;

    // Constructor (para crear personas fácilmente)
    public main(String nombre, int edad, String correo) {
        this.nombre = nombre;
        this.edad = edad;
        this.correo = correo;
    }

    // Métodos para mostrar los datos
    public void mostrarPersona() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Edad: " + edad);
        System.out.println("Correo: " + correo);
    }

    // Método para mostrar una sola línea (para la lista completa)
    public String resumen() {
        return nombre + " - " + edad + " años - " + correo;
    }
}
