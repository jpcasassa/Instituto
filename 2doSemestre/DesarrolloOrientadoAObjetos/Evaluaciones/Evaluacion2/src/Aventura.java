public class Aventura extends Excursion {
    private String deporte;
    private String equipamiento;

    public Aventura(String codigo, String nombre, int duracion, double precioBase, String dificultad, String deporte, String equipamiento) {
        super(codigo, nombre, duracion, precioBase, dificultad);
        this.deporte = deporte;
        this.equipamiento = equipamiento;
    }

    @Override
    public double calcularCostoAdicional() {
        double adicional = 0;
        // Si el deporte es rafting, se aumenta un 10%
        if (deporte.equalsIgnoreCase("rafting")) {
            adicional = precioBase * 0.10;
            precioBase += adicional;
        }
        return adicional;
    }

    @Override
    public double aplicarDescuento() {
        // Solo aplica descuento si dura más de 5 horas y la dificultad es alta
        if (duracion > 5 && dificultad.equalsIgnoreCase("alta")) {
            double descuento = precioBase * DTO_TEM;
            precioBase -= descuento;
            return descuento;
        }
        return 0;
    }

    @Override
    public void mostrarInfo() {
        super.mostrarInfo();
        System.out.println("Deporte: " + deporte + " | Equipamiento: " + equipamiento);
    }
}
