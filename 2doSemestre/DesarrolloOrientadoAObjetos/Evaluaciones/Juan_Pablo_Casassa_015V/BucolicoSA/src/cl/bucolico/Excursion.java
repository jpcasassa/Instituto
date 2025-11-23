package cl.bucolico;

// clase abstracta base que define atributos comunes a excursiones
public abstract class Excursion implements Promocion {
    // Encapsulación avanzada: variables protegidas para acceso desde las hijas
    protected String codigo;
    protected String nombre;
    protected int duracion; // en horas
    protected double precioBase;
    protected String dificultad; // baja, media o alta

    // Constructor para incializar todos los datos en comun
    public Excursion(String codigo, String nombre, int duracion, double precioBase, String dificultad) {
        this.codigo = codigo;
        this.nombre = nombre;
        this.duracion = duracion;
        this.precioBase = precioBase;
        this.dificultad = dificultad;
    }

    // Getters publicos
    public String getCodigo() {return codigo; }
    public double getPrecioBase() {return precioBase; }
    public String getDificultad() {return dificultad; }
    public int getDuracion() {return duracion; }

    // Metodo con logica interna controlada
    public void disminuirBase() {
        if (dificultad.equalsIgnoreCase("baja")) {
            precioBase -= precioBase * 0.10;
        }
    }

    // @Override: redefine el metodo abstracto
    public abstract double calcularCostoAdicional();

    // Metodo común: muestra la info basica de cualquier excursión
    public void mostrarInfo() {
        System.out.println("Codigo: " + codigo + "| Nombre: " + nombre);
        System.out.println("Duracion: " + duracion + "hrs | Dificultad: " + dificultad);
        System.out.println("Precio base: $" + precioBase);
    }
}
