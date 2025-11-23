package cl.bucolico;

// Clase hija: representa el tipo de excurcion
public class Aventura extends Excursion {
    private String deporte;
    private String equipamiento;

    public Aventura(String codigo, String nombre, int duracion, double precioBase, String dificultad, String deporte, String equipamiento) {
        super(codigo, nombre, duracion, precioBase, dificultad);
        this.deporte = deporte;
        this.equipamiento = equipamiento;
    }

    // @Override: redefine el metodo abstracto
    @Override
    public double calcularCostoAdicional() {
        double adicional = 0;
        if (deporte.equalsIgnoreCase("rafting")) {
            adicional = precioBase * 0.10;
            precioBase += adicional;
        }
        return adicional;
    }

    // Implementación del metodo de la interfaz
    @Override
    public double aplicarDescuento() {
        if (duracion > 5 && dificultad.equalsIgnoreCase("alta")) {
            double desc = precioBase * DTO_TEM;
            precioBase -= desc;
            return desc;
        }
        return 0;
    }

    @Override
    public void mostrarInfo() {
        super.mostrarInfo();
        System.out.println("Deporte: " + deporte + " | Equipamiento: " + equipamiento);
    }
}