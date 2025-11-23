import java.util.ArrayList;

public class Catalogo {
    private ArrayList<Excursion> lista = new ArrayList<>();

    public void agregarExcursion(Excursion e) {
        for (Excursion ex : lista) {
            if (ex.getCodigo().equalsIgnoreCase(e.getCodigo())) {
                System.out.println("❌ Código duplicado, no se agregó.");
                return;
            }
        }
        lista.add(e);
        System.out.println("✅ Excursión agregada con éxito.");
    }

    public Excursion buscarExcursion(String codigo) {
        for (Excursion e : lista) {
            if (e.getCodigo().equalsIgnoreCase(codigo))
                return e;
        }
        return null;
    }

    public void aplicarAjusteATodas() {
        for (Excursion e : lista) {
            e.disminuirBase();
        }
        System.out.println("🔄 Ajuste de precios aplicado a todas las excursiones.");
    }

    public double calcularDescuentoTotal() {
        double total = 0;
        for (Excursion e : lista) {
            total += e.aplicarDescuento();
        }
        return total;
    }

    public void eliminarExcursion(String codigo) {
        Excursion e = buscarExcursion(codigo);
        if (e != null) {
            lista.remove(e);
            System.out.println("🗑️ Excursión eliminada correctamente.");
        } else {
            System.out.println("⚠️ No se encontró una excursión con ese código.");
        }
    }

    public void mostrarTodas() {
        for (Excursion e : lista) {
            e.mostrarInfo();
            System.out.println("-----------------------------");
        }
    }
}
