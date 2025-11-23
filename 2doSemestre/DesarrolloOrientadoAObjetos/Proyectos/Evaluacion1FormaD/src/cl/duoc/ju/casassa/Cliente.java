package cl.duoc.ju.casassa;

public class Cliente {
    // Atributos
    private String nombre;
    private String rut;
    private int edad;

    public Cliente() {
    }

    public Cliente (String rut, String nombre, int edad){
        this.rut = rut;
        this.nombre = nombre;
        setNombre(nombre); // usamos el setter para validar
        setEdad(edad);
    }

    public String getRun() {
        return rut;
    }

    public void setRut(String rut) {
        this.rut = rut;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        if (nombre == null || nombre.trim().isEmpty()) {
            throw new IllegalArgumentException("El nombre del cliente no puede estar vacío.");
        }
        this.nombre = nombre;
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        if (edad <= 0) {
            throw new IllegalArgumentException("La edad debe ser mayor que 0.");
        }
        this.edad = edad;
    }

    // Método auxiliar para mostrar info del cliente
    @Override
    public String toString() {
        return "Cliente [RUT=" + rut + ", Nombre=" + nombre + ", Edad=" + edad + "]";
    }
}
