import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Catalogo c = new Catalogo();
        int opcion;

        do {
            System.out.println("\n--- Bucólico S.A ---");
            System.out.println("1. Ingresar Excursión");
            System.out.println("2. Mostrar Información");
            System.out.println("3. Aplicar Ajuste de Precio");
            System.out.println("4. Eliminar Excursión");
            System.out.println("5. Salir");
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
                        c.agregarExcursion(new Aventura(codigo, nombre, dur, precio, dif, dep, eq));
                    } else {
                        System.out.print("Destino histórico: ");
                        String des = sc.nextLine();
                        System.out.print("Idioma del guía: ");
                        String idi = sc.nextLine();
                        c.agregarExcursion(new Cultural(codigo, nombre, dur, precio, dif, des, idi));
                    }
                    break;

                case 2:
                    c.mostrarTodas();
                    break;

                case 3:
                    c.aplicarAjusteATodas();
                    System.out.println("Descuento total aplicado: $" + c.calcularDescuentoTotal());
                    break;

                case 4:
                    System.out.print("Código a eliminar: ");
                    String cod = sc.nextLine();
                    c.eliminarExcursion(cod);
                    break;
            }
        } while (opcion != 5);

        System.out.println("👋 Programa finalizado, gracias por usar Bucólico S.A.");
    }
}
