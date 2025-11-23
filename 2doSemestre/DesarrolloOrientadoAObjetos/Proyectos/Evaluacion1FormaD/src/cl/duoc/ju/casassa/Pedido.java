package cl.duoc.ju.casassa;

public class Pedido {
    private String fecha; // fecha del pedido
    private Cliente cliente; // cliente que hace el pedido
    private Artista artista; // artista responsable del cuadro
    private Cuadro cuadro; // cuadro solicitado
    private int cantidad; // cantidad solicitada
    private double totalBruto; // total antes de descuentos
    private double descuento; // descuento aplicado
    private double totalNeto; // total final después de descuento
    private boolean confirmado; // indica si el pedido está confirmado

    // Constructor
    public Pedido(String fecha, Cliente cliente, Artista artista, Cuadro cuadro, int cantidad) {
        this.fecha = fecha;
        this.cliente = cliente;
        this.artista = artista;
        this.cuadro = cuadro;
        this.cantidad = cantidad;
        this.confirmado = false;
        calcularTotal(); // calcula total al crear el pedido
    }

    // Getters y Setters
    public String getFecha() {
        return fecha;
    }

    public void setFecha(String fecha) {
        this.fecha = fecha;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

    public Artista getArtista() {
        return artista;
    }

    public void setArtista(Artista artista) {
        this.artista = artista;
    }

    public Cuadro getCuadro() {
        return cuadro;
    }

    public void setCuadro(Cuadro cuadro) {
        this.cuadro = cuadro;
    }

    public int getCantidad() {
        return cantidad;
    }

    public void setCantidad(int cantidad) {
        this.cantidad = cantidad;
        calcularTotal(); // recalcular totales si cambia la cantidad
    }

    public double getTotalBruto() {
        return totalBruto;
    }

    public double getDescuento() {
        return descuento;
    }

    public double getTotalNeto() {
        return totalNeto;
    }

    public boolean isConfirmado() {
        return confirmado;
    }

    public void setConfirmado(boolean confirmado) {
        this.confirmado = confirmado;
    }

    // Método que calcula el total bruto y total neto aplicando descuentos
    public void calcularTotal() {
        // Total bruto
        totalBruto = cantidad * cuadro.getPrecioUnitario();

        // Descuento según reglas
        descuento = 0;

        // Si cliente mayor de 65 años, 25% primero
        if (cliente.getEdad() > 65) {
            descuento += totalBruto * 0.25;
        }

        // Descuento por monto
        if (totalBruto >= 200000) {
            descuento += totalBruto * 0.15;
        } else if (totalBruto > 60000) {
            descuento += totalBruto * 0.05;
        }

        // Total neto
        totalNeto = totalBruto - descuento;

        // Confirmación del pedido
        confirmado = (cliente.getNombre() != null && !cliente.getNombre().isEmpty()) &&
                (artista.getNombre() != null && !artista.getNombre().isEmpty());
    }
}
