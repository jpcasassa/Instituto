package cl.duoc.ju.casassa;

public class Galeria {
    private int nroGaleria;
    private String nombre;
    private String ciudad;

    // Constructor
    public Galeria(int nroGaleria, String nombre, String ciudad) {
        this.nroGaleria = nroGaleria;
        this.nombre = nombre;
        this.ciudad = ciudad;
    }

    // Getters
    public int getNroGaleria() {
        return nroGaleria;
    }

    public String getNombre() {
        return nombre;
    }

    public String getCiudad() {
        return ciudad;
    }

    // Setters
    public void setNroGaleria(int nroGaleria) {
        this.nroGaleria = nroGaleria;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setCiudad(String ciudad) {
        this.ciudad = ciudad;
    }
}
