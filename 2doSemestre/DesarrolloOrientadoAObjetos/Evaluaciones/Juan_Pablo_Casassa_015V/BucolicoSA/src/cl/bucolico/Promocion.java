package cl.bucolico;

//define un "contrato" común para aplicar descuentos

public interface Promocion {
    public static final double DTO_TEM = 0.15; // Creamos una variable para descontar el 15%

    // Metodo que calcula descuento segun duracion y dificultad
    double aplicarDescuento();
}
