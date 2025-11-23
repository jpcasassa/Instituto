package cl.bucolico;
import java.util.ArrayList;

public class Catalogo {
    private ArrayList<Excursion> lista = new ArrayList<>();

    // Evita duplicados por código
    public void agregarExcursion(Excursion e) {
        for (Excursion ex : lista) {
            if (ex.getCodigo().equalsIgnoreCase(e.getCodigo())) {
                System.out.println("❌ Código duplicado, no se agregó.");
                return;
            }
        }
        lista.add(e);
        System.out.println("✅ Excursión agregada correctamente.");
    }

    public Excursion buscarExcursion(String codigo) {
        for (Excursion e : lista) {
            if (e.getCodigo().equalsIgnoreCase(codigo)) return e;
        }
        return null;
    }

    public void aplicarAjusteATodas() {
        for (Excursion e : lista) {
            e.disminuirBase();
        }
        System.out.println("🔧 Ajuste aplicado a todas las excursiones elegibles.");
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
            System.out.println("🗑️ Excursión eliminada.");
        } else {
            System.out.println("⚠️ No se encontró la excursión.");
        }
    }

    public void mostrarTodas() {
        if (lista.isEmpty()) {
            System.out.println("(No hay excursiones registradas)");
            return;
        }
        for (Excursion e : lista) {
            e.mostrarInfo();
            System.out.println("-----------------------------");
        }
    }
}
