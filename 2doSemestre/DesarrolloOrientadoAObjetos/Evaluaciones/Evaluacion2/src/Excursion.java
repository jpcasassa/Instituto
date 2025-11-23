public abstract class Excursion implements Promocion {
    protected String codigo;
    protected String nombre;
    protected int duracion;
    protected double precioBase;
    protected String dificultad;

    public Excursion(String codigo, String nombre, int duracion, double precioBase, String dificultad) {
        this.codigo = codigo;
        this.nombre = nombre;
        this.duracion = duracion;
        this.precioBase = precioBase;
        this.dificultad = dificultad;
    }

    public String getCodigo() { return codigo; }
    public double getPrecioBase() { return precioBase; }
    public String getDificultad() { return dificultad; }
    public int getDuracion() { return duracion; }

    // Si la dificultad es baja, se rebaja un 10% el precio base
    public void disminuirBase() {
        if (dificultad.equalsIgnoreCase("baja")) {
            precioBase -= precioBase * 0.10;
        }
    }

    // Cada tipo de excursión define su propio costo adicional
    public abstract double calcularCostoAdicional();

    // Muestra información básica de cualquier excursión
    public void mostrarInfo() {
        System.out.println("Código: " + codigo + " | Nombre: " + nombre);
        System.out.println("Duración: " + duracion + " hrs | Dificultad: " + dificultad);
        System.out.println("Precio base: $" + precioBase);
    }
}
