public interface Promocion {
    double DTO_TEM = 0.15; // 15% de descuento

    // Este método aplicará un descuento si la excursión dura más de 5 horas y es de dificultad alta.
    double aplicarDescuento();
}
