package sistemapedidos;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); // Crear un escáner para leer datos desde el teclado

        // VARIABLES SIMPLES PARA GUARDAR DATOS EN MEMORIA
        String nombreCliente = "";
        int edadCliente = 0;
        String rutCliente = "";
        String fechaNacimiento = "";

        String nombreVendedor = "";
        String rutVendedor = "";
        String region = "";

        String nombreProducto = "";
        String tipoProducto = "";
        double precioProducto = 0;

        int cantidad = 0;

        // BUCLE INFINITO PARA MOSTRAR EL MENÚ HASTA QUE EL USUARIO ELIJA SALIR
        while (true) {
            // MOSTRAR MENÚ
            System.out.println("=== SISTEMA DE PEDIDOS DE COSMETICOS ===");
            System.out.println("1. Ingresar Cliente");
            System.out.println("2. Ingresar Vendedor");
            System.out.println("3. Ingresar Producto");
            System.out.println("4. Generar Pedido");
            System.out.println("5. Salir");
            System.out.print("Seleccione una opción: ");
            int opcion = sc.nextInt();
            sc.nextLine(); // Limpiar buffer del teclado para evitar errores al leer strings después de números

            // OPCIÓN 1: INGRESAR CLIENTE
            if (opcion == 1) {
                System.out.println("--- INGRESO DE CLIENTE ---");
                System.out.print("Ingrese RUT: ");
                rutCliente = sc.nextLine(); // Guardar rut
                System.out.print("Ingrese nombre: ");
                nombreCliente = sc.nextLine(); // Guardar nombre
                System.out.print("Ingrese edad: ");
                edadCliente = sc.nextInt(); // Guardar edad
                sc.nextLine(); // Limpiar buffer
                System.out.print("Ingrese fecha de nacimiento (AAAA-MM-DD): ");
                fechaNacimiento = sc.nextLine(); // Guardar fecha de nacimiento
                System.out.println("Cliente registrado con éxito.\n");

                // OPCIÓN 2: INGRESAR VENDEDOR
            } else if (opcion == 2) {
                System.out.println("--- INGRESO DE VENDEDOR ---");
                System.out.print("Ingrese RUT: ");
                rutVendedor = sc.nextLine();
                System.out.print("Ingrese nombre: ");
                nombreVendedor = sc.nextLine();
                System.out.print("Ingrese región: ");
                region = sc.nextLine();
                System.out.println("Vendedor registrado con éxito.\n");

                // OPCIÓN 3: INGRESAR PRODUCTO
            } else if (opcion == 3) {
                System.out.println("--- INGRESO DE PRODUCTO ---");
                System.out.print("Ingrese nombre del producto: ");
                nombreProducto = sc.nextLine();
                System.out.print("Ingrese tipo (Crema/Perfume): ");
                tipoProducto = sc.nextLine();
                System.out.print("Ingrese precio unitario: ");
                precioProducto = sc.nextDouble();
                sc.nextLine();
                System.out.println("Producto registrado con éxito.\n");

                // OPCIÓN 4: GENERAR PEDIDO
            } else if (opcion == 4) {
                System.out.println("--- GENERAR PEDIDO ---");
                System.out.print("Ingrese cantidad: ");
                cantidad = sc.nextInt(); // Guardar cantidad
                sc.nextLine();

                // CALCULAR TOTAL BRUTO (cantidad * precio unitario)
                double totalBruto = cantidad * precioProducto;

                // CALCULAR DESCUENTO
                double descuento = 0;
                if (totalBruto > 100000) { // Si total > 100.000 → 20% de descuento
                    descuento = totalBruto * 0.2;
                } else if (totalBruto > 50000) { // Si total > 50.000 → 10% de descuento
                    descuento = totalBruto * 0.1;
                }

                // TOTAL NETO (total bruto - descuento)
                double totalNeto = totalBruto - descuento;

                // DETERMINAR ESTADO DEL PEDIDO
                String estado = "Pendiente"; // Inicialmente pendiente
                if (!nombreCliente.isEmpty() && edadCliente >= 18 && edadCliente < 100
                        && !nombreVendedor.isEmpty() && (tipoProducto.equals("Crema") || tipoProducto.equals("Perfume"))) {
                    estado = "Confirmado"; // Pedido confirmado si datos válidos
                }

                // MOSTRAR INFORMACIÓN DEL PEDIDO
                System.out.println("\n--- DETALLE DEL PEDIDO ---");
                System.out.println("Cliente: " + nombreCliente + " (" + edadCliente + " años)");
                System.out.println("Vendedor: " + nombreVendedor);
                System.out.println("Producto: " + nombreProducto + " (" + tipoProducto + ")");
                System.out.println("Cantidad: " + cantidad);
                System.out.println("Total bruto: $" + totalBruto);
                System.out.println("Descuento: $" + descuento);
                System.out.println("Total neto: $" + totalNeto);
                System.out.println("Estado: " + estado + "\n");

                // OPCIÓN 5: SALIR DEL SISTEMA
            } else if (opcion == 5) {
                System.out.println("Saliendo del sistema...");
                break; // Termina el bucle y cierra el programa

                // OPCIÓN INVÁLIDA
            } else {
                System.out.println("Opción inválida.\n");
            }
        }

        sc.close(); // Cerrar el escáner
    }
}
