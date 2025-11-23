package cl.duoc.ju.casassa;

public class Artista {
    // Atributos
    private String nombre;
    private String rut;
    private int nro_artista;
    private String fecha_de_ingreso;
    private String tipo_galeria;

    // Constructor vacío
    public Artista() {
    }

    // Constructor con parámetros
    public Artista(String nombre, String rut, int nro_artista, String fecha_de_ingreso, String tipo_galeria) {
        setNombre(nombre);
        this.rut = rut;
        this.nro_artista = nro_artista;
        setFecha_de_ingreso(fecha_de_ingreso);
        this.tipo_galeria = tipo_galeria;
    }

    // Getters
    public String getNombre() {
        return nombre;
    }

    public String getRut() {
        return rut;
    }

    public int getNro_artista() {
        return nro_artista;
    }

    public String getFecha_de_ingreso() {
        return fecha_de_ingreso;
    }

    public String getTipo_galeria() {
        return tipo_galeria;
    }

    // Setters
    public void setNombre(String nombre) {
        if (nombre == null || nombre.trim().isEmpty()) {
            throw new IllegalArgumentException("El nombre del artista no puede estar vacío.");
        }
        this.nombre = nombre;
    }

    public void setRut(String rut) {
        this.rut = rut;
    }

    public void setNro_artista(int nro_artista) {
        this.nro_artista = nro_artista;
    }

    public void setFecha_de_ingreso(String fecha_de_ingreso) {
        if (fecha_de_ingreso == null || fecha_de_ingreso.trim().isEmpty()) {
            throw new IllegalArgumentException("La fecha de ingreso no puede estar vacía.");
        }
        this.fecha_de_ingreso = fecha_de_ingreso;
    }

    public void setTipo_galeria(String tipo_galeria) {
        this.tipo_galeria = tipo_galeria;
    }

    // Método toString
    @Override
    public String toString() {
        return "Artista {" +
                "Nombre='" + nombre + '\'' +
                ", RUT='" + rut + '\'' +
                ", Nro Artista=" + nro_artista +
                ", Fecha de Ingreso='" + fecha_de_ingreso + '\'' +
                ", Tipo de Galería='" + tipo_galeria + '\'' +
                '}';
    }
}
