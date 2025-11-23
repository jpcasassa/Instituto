package cl.bucolico;

public class Cultural extends Excursion {
    private String destinoHistorico;
    private String idiomaGuia;

    public Cultural(String codigo, String nombre, int duracion, double precioBase, String dificultad, String destinoHistorico, String idiomaGuia) {
        super(codigo, nombre, duracion, precioBase, dificultad);
        this.destinoHistorico = destinoHistorico;
        this.idiomaGuia = idiomaGuia;
    }

    @Override
    public double calcularCostoAdicional() {
        double adicional = 0;
        if (idiomaGuia.equalsIgnoreCase("ingles")) {
            adicional = precioBase * 0.10;
            precioBase += adicional;
        }
        return adicional;
    }

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
        System.out.println("Destino histórico: " + destinoHistorico + " | Guía: " + idiomaGuia);
    }
}
