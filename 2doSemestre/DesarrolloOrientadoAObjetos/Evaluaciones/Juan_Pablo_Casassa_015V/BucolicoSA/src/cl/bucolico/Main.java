package cl.bucolico;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Catalogo catalogo = new Catalogo();
        int opcion;

        do {
            System.out.println("\n--- Bucólico S.A ---");
            System.out.println("1. Ingresar Excursión");
            System.out.println("2. Mostrar Excursiones");
            System.out.println("3. Aplicar Ajuste de Precio");
            System.out.println("4. Eliminar Excursión");
            System.out.println("5. Calcular Descuento Total");
            System.out.println("6. Salir");
            System.out.print("Elija opción: ");

            opcion = sc.nextInt(); sc.nextLine();

            switch (opcion) {
                case 1:
                    System.out.print("Tipo (Aventura/Cultural): ");
                    String tipo = sc.nextLine();

                    System.out.print("Código: ");
                    String codigo = sc.nextLine();

                    System.out.print("Nombre: ");
                    String nombre = sc.nextLine();

                    System.out.print("Duración (horas): ");
                    int dur = sc.nextInt();

                    System.out.print("Precio base: ");
                    double precio = sc.nextDouble();
                    sc.nextLine();

                    System.out.print("Dificultad (baja/media/alta): ");
                    String dif = sc.nextLine();

                    if (tipo.equalsIgnoreCase("Aventura")) {
                        System.out.print("Deporte: ");
                        String dep = sc.nextLine();
                        System.out.print("Equipamiento: ");
                        String eq = sc.nextLine();
                        Excursion e = new Aventura(codigo, nombre, dur, precio, dif, dep, eq);
                        e.calcularCostoAdicional();
                        catalogo.agregarExcursion(e);
                    } else {
                        System.out.print("Destino histórico: ");
                        String des = sc.nextLine();
                        System.out.print("Idioma del guía: ");
                        String idi = sc.nextLine();
                        Excursion e = new Cultural(codigo, nombre, dur, precio, dif, des, idi);
                        e.calcularCostoAdicional();
                        catalogo.agregarExcursion(e);
                    }
                    break;

                case 2:
                    catalogo.mostrarTodas();
                    break;

                case 3:
                    catalogo.aplicarAjusteATodas();
                    break;

                case 4:
                    System.out.print("Código a eliminar: ");
                    String cod = sc.nextLine();
                    catalogo.eliminarExcursion(cod);
                    break;

                case 5:
                    double total = catalogo.calcularDescuentoTotal();
                    System.out.println("Descuento total aplicado: $" + total);
                    break;

                case 6:
                    System.out.println("👋 Programa finalizado. Gracias!");
                    break;

                default:
                    System.out.println("Opción inválida, intente de nuevo.");
            }

        } while (opcion != 6);
    }
}
