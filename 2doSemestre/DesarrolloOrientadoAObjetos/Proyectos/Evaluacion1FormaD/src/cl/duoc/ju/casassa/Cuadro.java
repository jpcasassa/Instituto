package cl.duoc.ju.casassa;

public class Cuadro {

    // Atributos privados
    private int codigo;
    private String nombre;
    private String tecnica;
    private String tipoArte;
    private int precioUnitario;

    // Constructor
    public Cuadro(int codigo, String nombre, String tecnica, String tipoArte) {
        this.codigo = codigo;
        this.nombre = nombre;
        this.tecnica = tecnica;
        this.tipoArte = tipoArte;
        this.precioUnitario = asignarPrecio(tecnica, tipoArte);
    }

    // Método privado para calcular precio según la tabla
    private int asignarPrecio(String tecnica, String tipoArte) {
        if (tipoArte.equalsIgnoreCase("Moderno")) {
            if (tecnica.equalsIgnoreCase("Óleo")) return 70000;
            if (tecnica.equalsIgnoreCase("Acrílico")) return 60000;
            if (tecnica.equalsIgnoreCase("Carbón")) return 45000;
        } else if (tipoArte.equalsIgnoreCase("Clásico")) {
            if (tecnica.equalsIgnoreCase("Óleo")) return 90000;
            if (tecnica.equalsIgnoreCase("Acrílico")) return 75000;
            if (tecnica.equalsIgnoreCase("Carbón")) return 50000;
        } else if (tipoArte.equalsIgnoreCase("Contemporáneo")) {
            if (tecnica.equalsIgnoreCase("Óleo")) return 65000;
            if (tecnica.equalsIgnoreCase("Acrílico")) return 55000;
            if (tecnica.equalsIgnoreCase("Carbón")) return 40000;
        }
        return 0; // caso inválido
    }

    // Getters y Setters públicos
    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getTecnica() {
        return tecnica;
    }

    public void setTecnica(String tecnica) {
        this.tecnica = tecnica;
        this.precioUnitario = asignarPrecio(tecnica, this.tipoArte);
    }

    public String getTipoArte() {
        return tipoArte;
    }

    public void setTipoArte(String tipoArte) {
        this.tipoArte = tipoArte;
        this.precioUnitario = asignarPrecio(this.tecnica, tipoArte);
    }

    public int getPrecioUnitario() {
        return precioUnitario;
    }
}
